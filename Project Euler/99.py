from math import log2


def calc(a, b, c, d):
    return b * log2(a) >= d * log2(c)


f = open("./0099_base_exp.txt", "r")
S = [list(map(int, s.split(","))) for s in f.read().split("\n")]
T = [[i + 1, S[i][0], S[i][1]] for i in range(len(S))]
for i in range(len(T) - 1):
    for j in range(len(T) - 1):
        if calc(*T[j][1:], *T[j + 1][1:]):
            T[j], T[j + 1] = T[j + 1], T[j]
print(T[-1])
