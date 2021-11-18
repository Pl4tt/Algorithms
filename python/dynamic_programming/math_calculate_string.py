numeric_val = int | float

def is_precendenced(check_operator: str, base_operator: str) -> bool:
    if base_operator in "*/":
        return check_operator in "*/"
    
    return True

def _calculate(val1: numeric_val, operator: str, val2: numeric_val) -> numeric_val:
    match operator:
        case "+":
            return val1 + val2
        case "-":
            return val1 - val2
        case "*":
            return val1 * val2
        case "/":
            return val1 / val2

def calculate(calculation: str) -> numeric_val:
    allowed_operators = "+-*/"
    operator = []
    operands = []
    current_sign = ""

    while calculation:
        # first element is numeric
        if calculation[0].isnumeric():
            while calculation and (calculation[0].isnumeric() or calculation[0] == "." and not "." in current_sign):
                current_sign += calculation[0]
                calculation = calculation[1:]

            operands.append(current_sign)
            current_sign = ""

        # first element is an operator and not precendenced to the last operator
        elif operator and calculation[0] in allowed_operators and (not is_precendenced(calculation[0], operator[-1])):
            while operator and operator[-1] != "(":
                val2 = float(operands.pop())
                op = operator.pop()
                val1 = float(operands.pop())

                new_val = _calculate(val1, op, val2)
                operands.append(new_val)
        
        # first element is an operator and precendenced to the last operator
        elif not operator and calculation[0] in allowed_operators or calculation[0] in allowed_operators and (is_precendenced(calculation[0], operator[-1]) or operator[-1] in "()"):
            operator.append(calculation[0])
            calculation = calculation[1:]
        
        # first element is "("
        elif calculation[0] == "(":
            operator.append(calculation[0])
            calculation = calculation[1:]
        
        # first element is ")"
        elif calculation[0] == ")":
            calculation = calculation[1:]

            while operator and operator[-1] != "(":
                val2 = float(operands.pop())
                op = operator.pop()
                val1 = float(operands.pop())

                new_val = _calculate(val1, op, val2)
                operands.append(new_val)
            
            operator.pop()
        
        # first element is unusable sign
        else:
            calculation = calculation[1:]
    
    while operator and len(operands) >= 2:
        val2 = float(operands.pop())
        op = operator.pop()
        val1 = float(operands.pop())

        new_val = _calculate(val1, op, val2)
        operands.append(new_val)

    return operands[0]



if __name__ == "__main__":
    tests = {
        "1+1": 2,
        "3*5+1": 16,
        "5+2/4": 5.5,
        "3*3+3/3": 10,
        "(10 + 10) * 5/  10": 10,
        "5/5+( 1*2 +1.5) / 2": 2.75,
        "5-20*(10/(5 -  10))+(200 - 5) *(3 /  125)": 49.68,
        "(10+30)*(90.2/(59.3+(89.5)))*946+((2-46)-6*3)": 22875.956989247316,
    }

    for test, result in tests.items():
        print(calculate(test), result)
        assert calculate(test) == result