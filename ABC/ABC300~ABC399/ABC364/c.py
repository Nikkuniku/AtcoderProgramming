from itertools import accumulate

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
A = A[::-1]
B = B[::-1]
cuma = list(accumulate(A, initial=0))
cumb = list(accumulate(B, initial=0))
ans = N
for i in range(N + 1):
    if cuma[i] > X:
        ans = min(ans, i)
        break
for j in range(N + 1):
    if cumb[j] > Y:
        ans = min(ans, j)
        break
print(ans)
