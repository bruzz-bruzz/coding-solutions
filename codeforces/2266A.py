for _ in range(int(input())):
    n = int(input())
    s = [int(x) for x in str(input()).split(" ")]
    print(n - min(s))