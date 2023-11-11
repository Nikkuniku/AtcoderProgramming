a, b, c = map(int, input().split())
S = sorted([a, b, c])
ans = 'No'
if S[1] == b:
    ans = 'Yes'
print(ans)
