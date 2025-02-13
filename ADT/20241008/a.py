N = int(input())
S = []
A = []
for _ in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))
i = A.index(min(A))
ans = []
for k in range(N):
    ans.append(S[(i + k) % N])
print(*ans, sep="\n")
