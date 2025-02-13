N = int(input())
seen = set()
ans = []
for i in range(N):
    s = []
    for j in range(1, N + 1):
        if j in seen:
            continue
        s.append(j)
    l = 0
    r = len(s)
    while r - l > 1:
        mid = (l + r) // 2
        Q = ans[:]
        Q.append(s[mid])
        for m in s:
            if m != s[mid]:
                Q.append(m)
        print("?", *Q, flush=True, end="\n")
        ret = int(input())
        if ret == 1:
            l = mid
        else:
            r = mid
    ans.append(s[l])
    seen.add(s[l])
print("!", *ans, end="\n", flush=True)
