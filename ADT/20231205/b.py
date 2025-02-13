N = int(input())
tmp = 1 << 60
idx = -1
People = []
for i in range(N):
    S, A = input().split()
    A = int(A)
    if A < tmp:
        idx = i
        tmp = A
    People.append(S)
ans = []
for i in range(idx, N):
    ans.append(People[i])
for i in range(idx):
    ans.append(People[i])
print(*ans, sep="\n")
