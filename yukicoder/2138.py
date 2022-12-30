A, B, C, D, E = map(int, input().split())
ans = - 1 << 30
for i in range(C+1):
    ans = max(ans, A-B+(D-E)*i)
print(ans)
