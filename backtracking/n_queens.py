def n_queens(n):
    solutions = []
    state = []
    search(solutions, state, n)
    return solutions

def search(solutions, state, n):
    if len(state) == n:
        sol_str = to_string(state, n)
        solutions.append(sol_str)
        return # solution found
    
    for candidate in possible_candidates(state, n):
        state.append(candidate)
        search(solutions, state, n)
        state.pop()
    
def possible_candidates(state, n):
    if not state:
        return range(n)
    
    position = len(state)
    candidates = set(range(n))

    for row, col in enumerate(state):
        # check row and col
        candidates.discard(col)

        # check diagonal
        diag = position - row

        candidates.discard(col - diag)
        candidates.discard(col + diag)
    
    return candidates

def to_string(state, n):
    # [1, 3, 0, 2, 4] -> [".Q...", "...Q.", "Q....", "..Q..", "....Q"]
    result = []

    for pos in state:
        result.append("."*pos + "Q" + "."*(n - pos - 1))
    
    return result
