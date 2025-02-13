from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = SortedList(B)
A.sort(reverse=True)
seen = [False] * N
for i, v in enumerate(A):
    p = C.bisect_left(v)
    if p == len(C):
        continue
    seen[i] = True
    C.discard(C[p])
cnt = 0
for t in seen:
    cnt += not t
ans = -1
for i in range(N):
    if not seen[i]:
        ans = A[i]
        break
if cnt > 1:
    ans = -1
print(ans)
