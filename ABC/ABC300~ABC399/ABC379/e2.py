from itertools import accumulate

N = int(input())
S = input()
imos = [0] * (N + 1)
for i, v in enumerate(S):
    v = int(v)
    imos[i] += (i + 1) * v
    imos[-1] -= (i + 1) * v
cum = list(accumulate(imos))
cum.pop()
cum = cum[::-1]
ans = []
i = 0
while 1:
    p, q = cum[i] // 10, cum[i] % 10
    ans.append(q)
    if p > 0:
        if i + 1 < len(cum):
            cum[i + 1] += p
        else:
            cum.append(p)
    else:
        if i == len(cum) - 1:
            break
    i += 1
print(*ans[::-1], sep="")
