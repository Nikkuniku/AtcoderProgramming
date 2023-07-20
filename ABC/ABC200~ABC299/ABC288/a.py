N = int(input())
ans = []
for _ in range(N):
    a, b = map(int, input().split())
    ans.append(a+b)
print(*ans, sep="\n")
