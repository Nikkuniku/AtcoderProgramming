def solve(M, A):
    pass


ans = []
T = int(input())
for _ in range(T):
    M = int(input())
    A = list(map(int, input().split()))
    solve(M, A)
print(*ans, sep="\n")
