s=list(input())
n=len(s)


now=s[0]
cnt=0
for i in range(1,n):
    if s[i]==now:
        cnt+=1
        if s[i]=='0':
            s[i]='1'
            now='1'
        else:
            s[i]='0'
            now='0'
    else:
        now=s[i]

print(cnt)

