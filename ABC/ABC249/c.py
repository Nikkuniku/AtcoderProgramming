n, k = map(int, input().split())
ss = []
for i in range(n):
    ss.append(input())


def alpha_int(s):
    return ord(s)-97


ans = 0
for i in range(1 << n):
    cnt = 0
    sts = []
    alphabet = [0]*26
    for j in range(n):
        if (i >> j) & 1:
            cnt += 1
            sts.append(ss[j])
    if cnt < k:
        continue
    for p in sts:
        for i in range(len(p)):
            alphabet[alpha_int(p[i])] += 1
    tmp = 0
    for i in range(26):
        if alphabet[i] == k:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
