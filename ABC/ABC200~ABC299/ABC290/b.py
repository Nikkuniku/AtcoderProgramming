N, K = map(int, input().split())
S = input()
ans = []
cnt = 0
for i in range(N):
    if cnt < K:
        if S[i] == 'o':
            cnt += 1
        ans.append(S[i])
    else:
        ans.append('x')
print(''.join(ans))
