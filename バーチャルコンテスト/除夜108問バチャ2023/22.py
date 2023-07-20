A, B, C, X = map(int, input().split())
ans = 0
if X <= A:
    ans = 1
elif A+1 <= X <= B:
    ans = C/(B-A)
print(ans)
