A, B, C, K = map(int, input().split())
ans = pow(-1, K)*(A-B)
if abs(ans) > pow(10, 18):
    ans = 'Unfair'
print(ans)
