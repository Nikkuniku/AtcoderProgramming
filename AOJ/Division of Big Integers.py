A, B = map(int, input().split())
ans = 0
if (A >= 0 and B >= 0) or (A < 0 and B < 0):
    ans = abs(A)//abs(B)
elif A < 0 and B >= 0:
    ans = -(abs(A)//B)
elif A >= 0 and B < 0:
    ans = -(A//abs(B))
print(ans)
