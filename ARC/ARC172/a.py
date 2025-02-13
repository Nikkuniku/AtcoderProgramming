H, W, N = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
S = [(H, W)]
ans = "Yes"
for a in A:
    for i in range(len(S)):
        h, w = S[i]
        if h >= 2**a and w >= 2**a:
            t1 = [(h - 2**a, w), (2**a, w - 2**a)]
            t2 = [(w - 2**a, h), (2**a, h - 2**a)]
            T1 = max([s * t for s, t in t1])
            T2 = max([s * t for s, t in t2])
            S.pop(i)
            if T1 >= T2:
                S += t1
            else:
                S += t2
            break
    else:
        ans = "No"
print(ans)
