N, A, B = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 'No'
if S[A][B] == 'o':
    ans = 'Yes'
print(ans)
