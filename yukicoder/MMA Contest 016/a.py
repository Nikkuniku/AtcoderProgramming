A, B, C = map(int, input().split())
X = 2*(A*B+A*C+B*C)
Y = A*B*C
ans = 3
if X > Y:
    ans = 2
print(ans)
