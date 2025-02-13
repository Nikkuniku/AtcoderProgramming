from collections import Counter

N, M = map(int, input().split())
A = Counter(list(map(int, input().split())))
B = list(map(int, input().split()))
ans = "Yes"
for b in B:
    if A[b] > 0:
        A[b] -= 1
    else:
        ans = "No"
print(ans)
