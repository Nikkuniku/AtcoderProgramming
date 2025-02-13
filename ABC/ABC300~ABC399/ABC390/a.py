A = list(map(int, input().split()))
B = sorted(A)
ans = "No"
for i in range(4):
    C = A[:]
    C[i], C[i + 1] = C[i + 1], C[i]
    if C == B:
        ans = "Yes"
print(ans)
