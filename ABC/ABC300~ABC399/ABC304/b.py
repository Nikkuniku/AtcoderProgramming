N = list(input())
ans = []
if len(N) <= 3:
    ans = N
else:
    for i in range(len(N)):
        if i <= 2:
            ans.append(N[i])
        else:
            ans.append('0')
print(''.join(ans))
