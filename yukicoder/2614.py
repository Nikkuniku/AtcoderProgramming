from collections import deque


def solve(N):
    q = deque(list("ABC"))
    for _ in range(N - 1):
        C = q.pop()
        q.append("A")
        q.append(C)
        q.append("B")
        q.append("C")
    return "".join(q)


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    ans.append(solve(N))
print(*ans, sep="\n")
