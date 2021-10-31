# 1, 2, 3, 4, 5, 6, 7,  8,  9,  ...
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(n: int) -> int:
    """normal fibonacci solving algorithm"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fast_fibonacci(n: int, memo=None) -> int:
    """faster fibonacci solving algorithm using memorization"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fast_fibonacci(n-1, memo) + fast_fibonacci(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    # print(fibonacci(100)) # takes too long
    print(fast_fibonacci(100))
