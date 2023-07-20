S = list(input())
ans = 'no'
if len(S) == len(set(S)):
    ans = 'yes'
print(ans)
