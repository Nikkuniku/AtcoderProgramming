from sortedcontainers import SortedList

N = int(input())
H = list(map(int, input().split()))
stack = []
Pos = [-1] * N
for i in range(N - 1, -1, -1):
    while stack and stack[-1][1] < H[i]:
        j, t = stack.pop()
        Pos[j] = i
    stack.append((i, H[i]))
S = SortedList(Pos)
ans = []
for i in range(N):
    S.discard(Pos[i])
    res = S.bisect_right(i)
    ans.append(res)
print(*ans)
