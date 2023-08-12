from bisect import bisect_left
A, B = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
Numbers = [[] for _ in range(1001)]
for i in range(A):
    Numbers[S[i]].append(i)
ans = 0
for i in range(B):
    tmp = 0
    pre = -2
    for j in range(B):
        if i+j >= B:
            break
        idx = bisect_left(Numbers[T[i+j]], pre+1)
        if idx == len(Numbers[T[i+j]]):
            break
        pre = Numbers[T[i+j]][idx]
        tmp += 1
    ans = max(ans, tmp)
print(ans)
