N, A, B = map(int, input().split())
C = list(map(int, input().split()))
ans = C.index(A+B)+1
print(ans)
