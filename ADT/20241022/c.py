A, B = input().split()
A = A[::-1]
B = B[::-1]
ans = "Easy"
for i in range(min((len(A), len(B)))):
    s = int(A[i])
    t = int(B[i])
    if s + t >= 10:
        ans = "Hard"
print(ans)
