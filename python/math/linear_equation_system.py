from typing import Iterator, Any
from collections import defaultdict

class LinearEquationSolver:
    """Solves an n by n linear equation system with n unknowns.
    It can handle + and -, but not * and / and braces."""
    def __init__(self, equation_system: list[str], variables: list[str]) -> None:
        self.variables = variables
        self.variable_count = len(self.variables)
        self.equation_system = self._clean_equation_system(equation_system)
        self.equation_matrix = self._create_equation_matrix()  # the equation in form of a matrix
        self._swap_rows()
        self.alphabetical_matrix = [*self.variables, "*res*"]  # creates a matrix of all alphabetical characters
        self.solved_values = self.solve_gauss()  # the solved values as a dictionary

    def __str__(self) -> str:
        return "\nEquation System:\n" + "\n".join(self.equation_system) + "\n"
    
    def __len__(self) -> int:
        return self.variable_count

    def __getitem__(self, key: str) -> float:
        return self.solved_values.get(key, None)

    def __iter__(self) -> Iterator[tuple[str, float]]:
        for key, value in self.solved_values.items():
            yield key, value
    
    def __contains__(self, item: Any) -> bool:
        return item in self.variables

    def __round__(self, n: int=1) -> dict:
        return {k: round(v, n) for k, v in self.solved_values.items()}
    
    def _calculate(self, equation: str) -> str:
        """returns the given equation in the following pattern:
        all_alphabetical_values_sorted_by_self.values = the_numeric_value"""
        operators = "+-"
        elements = {k: 0 for k in self.variables}
        elements["*numeric*"] = 0
        eq_first, eq_second = equation.split("=")
        new_equation = ""
        numeric_key = "*numeric*"
        
        for i, char in enumerate(eq_first):
            if char in operators:
                num_str = ""
                c = 1

                while i+c < len(eq_first) and (eq_first[i+c].isnumeric() or eq_first[i+c] == "."):
                    num_str += eq_first[i+c]
                    c += 1
                    
                if i+c < len(eq_first) and eq_first[i+c] not in operators:
                    elements[eq_first[i+c]] += float(f"{char}{num_str}")
                else:
                    elements[numeric_key] -= float(f"{char}{num_str}")
                    
        for i, char in enumerate(eq_second):
            if char in operators:
                num_str = ""
                c = 1

                while i+c < len(eq_second) and (eq_second[i+c].isnumeric() or eq_second[i+c] == "."):
                    num_str += eq_second[i+c]
                    c += 1
                    
                if i+c < len(eq_second) and eq_second[i+c] not in operators:
                    elements[eq_second[i+c]] -= float(f"{char}{num_str}")
                else:
                    elements[numeric_key] += float(f"{char}{num_str}")

        for var in self.variables:
            if elements[var] >= 0:
                new_equation += f"+{+elements[var]}{var}"
            else:
                new_equation += str(elements[var]) + var

        if elements[numeric_key] >= 0:
            new_equation += f"=+{+elements[numeric_key]}"
        else:
            new_equation += f"={str(elements[numeric_key])}"
            
        return new_equation

    def _swap_rows(self) -> None:
        """swaps rows of the self.equation_system and self.equation_matrix if any swap is needed."""
        BASE_VALUE = self.equation_matrix[0][0]
        base_check_value = self.equation_matrix[1][0] * self.equation_matrix[0][1]
        check_value = BASE_VALUE * self.equation_matrix[1][1]

        c = 2  # to avoid infinite loops

        while len(self.equation_matrix) > 2 and base_check_value - check_value == 0 and c < len(self.equation_matrix):
            self.equation_matrix.append(self.equation_matrix[1])
            self.equation_system.append(self.equation_system[1])
            del self.equation_matrix[1]
            del self.equation_system[1]

            base_check_value = self.equation_matrix[1][0] * self.equation_matrix[0][1]
            check_value = BASE_VALUE * self.equation_matrix[1][1]

            c += 1
        
        if len(self.equation_matrix) == 2 and base_check_value - check_value == 0:
            self.equation_matrix[1], self.equation_matrix[0] = self.equation_matrix[0], self.equation_matrix[1]
            self.equation_system[1], self.equation_system[0] = self.equation_system[0], self.equation_system[1]
        
    def _clean_equation_system(self, eq_system: list[str]) -> list[str]:
        """replaces all none sign positions with a +, all whitespaces with empty string,
        places a 1 in front of only-character numers (x -> 1x) and uses the self._calculate
        function on every line in eq_system."""

        for i in range(len(eq_system)):
            eq_system[i] = eq_system[i].replace(" ", "")
            equal_index = eq_system[i].index("=")
            
            if eq_system[i][equal_index+1] not in "+-":
                eq_system[i] = f"{eq_system[i][:equal_index+1]}+{eq_system[i][equal_index+1:]}"
                
            if eq_system[i][0] not in "+-":
                eq_system[i] = f"+{eq_system[i]}"
                
            char = 0
            while char < len(eq_system[i]):
                if eq_system[i][char] in "+-":
                    if not eq_system[i][char+1].isnumeric():
                        eq_system[i] = f"{eq_system[i][:char+1]}1{eq_system[i][char+1:]}"
                        
                char += 1
                
            eq_system[i] = self._calculate(eq_system[i])
                        
        return eq_system

    def _create_equation_matrix(self) -> list[list[float]]:
        """returns a matrix including all numeric values of
        the equation system al a list of floats"""

        matrix = []

        for ind, equation in enumerate(self.equation_system):
            matrix.append([])
            
            for i, char in enumerate(equation):
                if char == "+":
                    c = 1
                    while i+c < len(equation) and (equation[i+c].isnumeric() or equation[i+c] == "."):
                        c += 1
                        
                    matrix[ind].append(float(equation[i+1:i+c]))
                
                elif char == "-":
                    c = 1
                    while i+c < len(equation) and (equation[i+c].isnumeric() or equation[i+c] == "."):
                        c += 1
                        
                    matrix[ind].append(float(equation[i:i+c]))

        return matrix

    def solve_equation_matrix(self) -> list[list[float]]:
        """updates the equation_matrix using the gauss algorithm
        and also returns the new matrix"""
        for i in range(1, len(self.equation_matrix)):
            base_value = self.equation_matrix[i-1][i-1]
            copy_matrix = self.equation_matrix[:]
            
            for equation in range(i, i+len(self.equation_matrix[i:])):
                eq_base_value = self.equation_matrix[equation][i-1]

                for val in range(len(self.equation_matrix[equation])):
                    new_val = eq_base_value * self.equation_matrix[i-1][val] - base_value * self.equation_matrix[equation][val]
                    copy_matrix[equation][val] = new_val
        
        self.equation_matrix = copy_matrix[:]
        return self.equation_matrix

    def solve_gauss(self) -> dict:
        """solves the self.equation_system using the gauss algorithm
        and returns a dictionary containing the variables and their values."""
        solved_values = self.solve_equation_matrix()
        equality_dicts = [defaultdict(float) for _ in range(len(solved_values))]
        return_dict = dict()
        
        for x in range(len(solved_values)-1, -1, -1):  # backwards through all lists of floats in solved_values
            new_var = self.alphabetical_matrix[x]
            equality_dicts[x]["*res*"] = 0.0
            equality_dicts[x]["*numeric*"] = 0.0
            
            for y in range(len(solved_values[x])-1, -1, -1):  # backwards through every element in list of floats x

                equality_dicts[x][self.alphabetical_matrix[y]] += solved_values[x][y]

                if self.alphabetical_matrix[y] == new_var:
                    return_dict[new_var] = (equality_dicts[x]["*res*"] + equality_dicts[x]["*numeric*"]*-1.0) / solved_values[x][y]
                    break

                elif self.alphabetical_matrix[y] != "*res*":
                    equality_dicts[x]["*numeric*"] += solved_values[x][y] * return_dict.get(self.alphabetical_matrix[y])

        return return_dict



