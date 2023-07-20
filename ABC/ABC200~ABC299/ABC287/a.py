N = int(input())
S = [input() for _ in range(N)]
ans = 'No'
if S.count('For') > N//2:
    ans = 'Yes'
print(ans)
