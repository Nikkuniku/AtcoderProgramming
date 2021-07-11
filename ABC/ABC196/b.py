x=list(input())

ans=''
if '.' not in x:
    ans = ''.join(x)
else:
    for i in range(len(x)):
        if x[i]=='.':
            break

        ans+=x[i]


print(ans)