N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))
ans = []

s = set()
for i in range(N):
    for j in range(M):
        for k in range(L):
            tmp = A[i] + B[j] + C[k]
            s.add(tmp)

for x in X:
    if x in s:
        ans.append("Yes")
    else:
        ans.append("No")
print(*ans, sep="\n")
