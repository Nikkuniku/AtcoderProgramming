H, W = map(int, input().split())
S = list(zip(*[list(input()) for _ in range(H)]))
T = list(zip(*[list(input()) for _ in range(H)]))
S.sort()
T.sort()
ans = 'Yes'
if S != T:
    ans = 'No'
print(ans)
