def count_construct(target: str, words: list, memo: dict=None) -> int:
    if memo is None:
        memo = {}
    
    if target in memo:
        return memo[target]
    if target == "":
        return 1

    total = 0

    for word in words:
        if target.startswith(word):
            new_target = target.replace(word, "", 1)
            new_target_total = count_construct(new_target, words, memo)
            total += new_target_total
    
    memo[target] = total
    return total





if __name__ == "__main__":
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcde"])) # True
    print(count_construct("xyz", ["ab", "cd", "ef", "x", "z", "y"])) # True
    print(count_construct("skateboard", ["sk", "bo", "rd", "skat", "skateboar", "sk", "boar", "bska", "ska"])) # False
    print(count_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printable", "print"])) # False
    print(count_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printble", "print", "b"])) # True
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeee", ["eeeeeeeeeeeeeeeeee", "eee", "e", "eeeeeeeeeeeeeeeeeeeee", "eeeeee", "e"])) # True
    print(count_construct("eeeeeeeeeeeeeee", ["EE", "E", "E", "EE", "E", "E", "EE", "E", "E", "EE", "E", "E"])) # False