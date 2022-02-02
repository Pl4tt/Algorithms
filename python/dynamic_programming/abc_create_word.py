def recursive_is_valid(s, t=None, memo=None):
    if memo is None:
        memo = {}
    if t is None:
        t = ""

    if t in memo:
        return memo[t]
    if s == t:
        return True
    if len(t) > len(s):
        return False
    
    for i in range(len(t)+1):
        new_t = t[:i+1] + "abc" + t[i+1:]
        
        if recursive_is_valid(s, new_t, memo):
            memo[t] = True
            return True
    
    memo[t] = False
    return False

def fast_is_valid(s):
    while "abc" in s:
        s = s.replace("abc", "")
    
    return not s





if __name__ == "__main__":
    print(fast_is_valid("aabcbc"))  # True
    print(fast_is_valid("abcabcababcc"))  # True
    print(fast_is_valid("abccba"))  # False
    print(fast_is_valid("abcabcabcabcabcabcabcabcabcabc"))  # True