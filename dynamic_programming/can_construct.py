def can_construct(target: str, words: list, memo: dict=None) -> bool:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == "":
        return True
    
    for word in words:
        if word in target:
            new_target = target.replace(word, "", 1)
            if can_construct(new_target, words, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False




if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcde"]))
    print(can_construct("xyz", ["ab", "cd", "ef", "x", "z", "y"]))
    print(can_construct("skateboard", ["sk", "bo", "rd", "skat", "skateboar", "sk", "boar", "bska", "ska"]))
    print(can_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printable", "print"]))
    print(can_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printble", "print", "b"]))
    print(can_construct("eeeeeeeeeeeeeeeeeeeeeeee", ["eeeeeeeeeeeeeeeeee", "eee", "e", "eeeeeeeeeeeeeeeeeeeee", "eeeeee", "e"]))
    print(can_construct("eeeeeeeeeeeeeee", ["EE", "E", "E", "EE", "E", "E", "EE", "E", "E", "EE", "E", "E"]))