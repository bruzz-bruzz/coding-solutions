def letterCombinations(digits: str) -> list[str]:
    og = len(digits)
    d = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
    }
    digits = list(digits)
    res = [x for x in d[digits.pop(0)]]
    while digits:
        p = digits.pop(0)
        for x in d[p]:
            for y in range(len(res)):
                if len(res[y]) == og:
                    res.append(res[y][:len(res[y]) - 1] + x)
                else:
                    res[y] += x
    res = list(set(res))
    return res
d = '2'
print(letterCombinations(d))