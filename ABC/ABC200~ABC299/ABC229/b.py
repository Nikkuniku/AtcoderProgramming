A, B = input().split()
M = min(len(A), len(B))
A = A[::-1]
B = B[::-1]
ans = 'Easy'
for i in range(M):
    a = int(A[i])
    b = int(B[i])
    if a+b >= 10:
        ans = 'Hard'
print(ans)
