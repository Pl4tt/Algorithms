def all_construct(target: str, words: list, memo: dict=None) -> list:
    if memo is None:
        memo = {}
    
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    
    total = []

    for word in words:
        if target.startswith(word):
            new_target = target.replace(word, "", 1)
            new_target_res = all_construct(new_target, words, memo)

            new_target_res = list(map(lambda way: way + [word], new_target_res))

            total.extend(new_target_res)
    
    memo[target] = total
    return total




if __name__ == "__main__":
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcde"]))
    print(all_construct("xyz", ["ab", "cd", "ef", "x", "z", "y"]))
    print(all_construct("skateboard", ["sk", "bo", "rd", "skat", "skateboar", "sk", "boar", "bska", "ska"]))
    print(all_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printable", "print"]))
    print(all_construct("printableprintoble", ["able", "ab", "le", "pr", "print", "rint", "ab", "printo", "printble", "print", "b"]))

