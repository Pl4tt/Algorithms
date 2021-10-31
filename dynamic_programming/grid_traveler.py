# (0, 0), (1, 1), (1, 3), (3, 3), (4, 5)
# 0,      1,      1,      4,      35

def grid_traveler(n: int, m: int, memo=None) -> int:
    if memo is None:
        memo = {}

    key = (min(n, m), max(n, m))

    if key in memo:
        return memo[key]
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    
    memo[key] = grid_traveler(n-1, m, memo) + grid_traveler(n, m-1, memo)
    return memo[key]

print(grid_traveler(100, 100))