def _generate_parentheses(opened: int, closed: int, temp: str, result: list) -> list:
    """Modifies the given result list to include all combinations of parentheses
    with opened opened parentheses and closed closed parentheses."""
    if opened == closed == 0:
        result.append(temp)
        return
    if opened > 0:
        _generate_parentheses(opened-1, closed, temp+"(", result)
    if closed > opened:
        _generate_parentheses(opened, closed-1, temp+")", result)

def generate_parentheses(n: int) -> list[str]:
    """returns all combinations of n parentheses"""
    solutions = []
    _generate_parentheses(n, n, "", solutions)
    return solutions





if __name__ == "__main__":
    print(generate_parentheses(0))
    print(generate_parentheses(1))
    print(generate_parentheses(2))
    print(generate_parentheses(3))
    print(generate_parentheses(4))
    print(generate_parentheses(5))
    