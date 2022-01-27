import math


def cbrt(x: float | int) -> float | int:
    """returns the cubic root of the given number x"""
    if x >= 0:
        return (x)**(1/3)
    else:
        return -((-x)**(1/3))

def create_value_dict(equation: str) -> dict:
    """returns a dictionary with the values of all variable exponents
    example input: create_value_dict('+1z^3-3.0z^2+3.0z-1.0+3.0z^2-6.0z+3.0-8.0z+8.0+4.0')
    example output: {'^3': 1.0, '^2': 0.0, '^1': -11.0, '^0': 14.0}\n
    it can also handle values of equations
    example input: create_value_dict('+5x^3+15x^2-40x+10=-10')
    example output: {'^3': 5.0, '^2': 15.0, '^1': -40.0, '^0': 20.0}\n
    in the case of an equation it moves all values to the left side
    (in this example it makes +10 on both sides to make the right side 0)"""

    state = 0
    values = {
        "^3": 0,
        "^2": 0,
        "^1": 0,
        "^0": 0,
    }

    for i, char in enumerate(equation):
        if char == "=":
            state = 1
        
        elif char in "+-":
            value = char
            
            j = 1
            while i+j < len(equation) and (equation[i+j].isnumeric() or equation[i+j] == "."):
                value += equation[i+j]
                j += 1
            
            key = ""
            while i+j < len(equation) and (equation[i+j].isalpha() or equation[i+j] == "^"):
                key += equation[i+j]
                j += 1
            
            key = key.replace("+", "")
            key = key.replace("-", "")
            
            if state == 0:
                if not key:
                    values["^0"] += float(value)
                elif key[-1] != "^":
                    values["^1"] += float(value)
                else:
                    values["^" + equation[i+j]] += float(value)
            
            elif state == 1:
                if not key:
                    values["^0"] -= float(value)
                elif key[-1] != "^":
                    values["^1"] -= float(value)
                else:
                    values["^" + equation[i+j]] -= float(value)

    return values

def normalize_equation(equation: str) -> tuple[str | float]:
    """normalizes the given equation\n
    example input: normalize_equation('+5x^3+15x^2-40x+10=-10', 'x')
    example output: ['+z^3-14z+14=0', -1]\n
    explaination:
        the first element in the output is the normalized form of the given equation
    \tthe second element is the equation to solve x using z (x=z-1 in example)"""
    
    values = create_value_dict(equation)
    
    divider = values["^3"]

    for k, _ in values.items():
        values[k] /= divider

    z = -values["^2"]/3

    new_3 = f"+1z^3+{3*z}z^2+{3*z**2}z+{z**3}".replace("+-", "-")
    new_2 = f"+{values['^2']}z^2+{2*values['^2']*z}z+{values['^2']*z**2}".replace("+-", "-")
    new_1 = f"+{values['^1']}z+{z*values['^1']}".replace("+-", "-")
    new_0 = f"+{values['^0']}".replace("+-", "-")
    
    new_values = create_value_dict(new_3+new_2+new_1+new_0)
    
    if new_values['^2'] != 0:
        raise RuntimeError("Not able to solve the equation yet :(")

    new_equation = f"+{new_values['^3']}z^3+{new_values['^1']}z+{new_values['^0']}=0".replace("+-", "-")
    
    return new_equation, z

def preprocess_start(revoice: str) -> str:
    """adds plus to start if needed"""
    revoice = revoice.replace(" ", "")

    if revoice[0] in "-+":
        return revoice
    return "+" + revoice

def preprocess_equation(equation: str) -> tuple[str | float]:
    """preprocesses the given equation"""
    
    first, second = equation.split("=")

    first = preprocess_start(first)
    second = preprocess_start(second)
    equation = f"{first}={second}"

    i = 0

    while i < len(equation):
        char = equation[i]
        
        if char in "+-" and not equation[i+1].isnumeric():
            equation = f"{equation[:i+1]}1{equation[i+1:]}"  # adds 1's before letters (x -> 1x)

        i += 1
        
    equation, z = normalize_equation(equation)

    return equation, z

def get_p_q(equation: str) -> tuple[float]:
    """returns the p and q parts of the given equation as a tuple (p, q)"""
    equation = equation.split("=")[0]
    parts = []
    
    for char in equation:
        if char in "+-":
            parts.append(char)
        
        elif char.isnumeric() or char == ".":
            parts[-1] += char

    cleaned_parts = tuple(map(lambda num: float(num), parts))
    
    return cleaned_parts

def use_cardano(p: float, q: float) -> float | None:
    """uses the cardano formula on the given p and q
    and returns the result if there is not root of -1"""

    root_val = (q/2)**2 + (p/3)**3
    
    if root_val < 0:
        return None

    result = cbrt(-(q/2) + math.sqrt(root_val)) + cbrt(-(q/2) - math.sqrt(root_val))

    return result

def use_imaginary_nums(p: float, q: float) -> list[float] | None:
    """uses imaginary numbers (and trigonometry) to solve the given p and q
    example input: use_imaginary_nums(-15, -4)
    example output: [4.0, -3.7320508075688767, -0.26794919243112464]"""
    root_val = (q/2)**2 + (p/3)**3
    
    if root_val >= 0:
        return None
    
    imaginary_num = math.sqrt(-root_val)
    real_num = -(q/2)

    long_side_len = math.sqrt(real_num**2 + imaginary_num**2)
    angle = math.atan2(imaginary_num, real_num)
    degree_angle = math.degrees(angle)
    divider = 180 / degree_angle
    
    first_value = 2 * (cbrt(long_side_len) * math.cos(math.pi/(divider*3)))
    second_value = 2 * (cbrt(long_side_len) * math.cos(math.pi/(divider*3) + 2*math.pi/3))
    third_value = 2 * (cbrt(long_side_len) * math.cos(math.pi/(divider*3) + 4*math.pi/3))
    
    return [first_value, second_value, third_value]

def solve_cubic_equation(equation: str) -> list[float]:
    """solves a cubic equation using the cardano formula
    and returns a list of all result values of the given variable.\n
    example input: solve_cardano('x^3-15x-126=0', 'x')
    example output: [6.0] (x=6)\n
    equations like '+5x^3+15x^2-40x+10=-10' would also work
    and return [1.0, -4.8284271, 0.8284271] in this case."""

    equation, z = preprocess_equation(equation)
    print(equation)
    p, q = get_p_q(equation[7:])
    
    solutions = []

    first_sol = use_cardano(p, q)

    if first_sol:
        solutions.append(first_sol)
    else:
        solutions = use_imaginary_nums(p, q)
    print(solutions, z)
    return list(map(lambda sol: round(sol + z, 7), solutions))







