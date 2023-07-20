X, A, B = map(int, input().split())
ans = 'dangerous'
if B <= A:
    ans = 'delicious'
elif A < B <= A+X:
    ans = 'safe'
print(ans)
