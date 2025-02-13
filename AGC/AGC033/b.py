H, W, N = map(int, input().split())
sr, sc = map(int, input().split())
S = input()
T = input()


def judge(s, t, n, sr, sc):
    res = False
    from itertools import product

    takahashi = list(product(range(2), repeat=n))
    aoki = list(product(range(2), repeat=n))
    for p1 in takahashi:
        for p2 in aoki:
            tr = sr
            tc = sc
            for i in range(n):
                a = p1[i]
                b = p2[i]
                if a == 1:
                    if s[i] == "R":
                        tc += 1
                    elif s[i] == "L":
                        tc -= 1
                    elif s[i] == "U":
                        tr += 1
                    elif s[i] == "D":
                        tr -= 1
                if not (1 <= tr <= n and 1 <= tc <= n):
                    break
                if b == 1:
                    if t[i] == "R":
                        tc += 1
                    elif t[i] == "L":
                        tc -= 1
                    elif t[i] == "U":
                        tr += 1
                    elif t[i] == "D":
                        tr -= 1
                if not (1 <= tr <= n and 1 <= tc <= n):
                    break
            res = True
    return res


print(judge(S, T, N, sr, sc))
