N = int(input())
T = list(map(int, input().split()))
S = sum(T)
M = int(input())
ans = []
for _ in range(M):
    p, x = map(int, input().split())
    p -= 1
    diff = x - T[p]
    ans.append(S + diff)
print(*ans, sep="\n")
