T = int(input())
ans = []
for _ in range(T):
    N, M = map(int, input().split())
    s = (N * (N + 1)) % M
    if 1 <= s <= N:
        ans.append("Bob")
    else:
        ans.append("Alice")
print(*ans, sep="\n")
