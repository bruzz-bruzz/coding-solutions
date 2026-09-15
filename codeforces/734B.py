s = str(input()).split(' ')
twoNums,threeNums,fiveNums,sixNums = int(s[0]), int(s[1]), int(s[2]),int(s[3])
def twofivesix(two,three,five,six):
    m = min(two,five,six)
    s = m * 256
    two -= m
    five -= m
    six -= m
    m = min(three,two)
    s += m * 32
    return s
def threetwo(two,three,five,six):
    m = min(three,two)
    s = m * 32
    two -= m
    three -= m
    m = min(two,five,six)
    s += m * 256
    return s
print(max(twofivesix(twoNums,threeNums,fiveNums,sixNums),threetwo(twoNums,threeNums,fiveNums,sixNums)))