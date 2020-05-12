s= list(input())
n= len(s)

children=[0]*n

cnt=0
for i in range(n-1):
    if s[i]=='R':
        cnt+=1

        if s[i+1]=='L':
            children[i]+=(cnt+1)//2
            children[i+1]+=cnt//2

    else:
        cnt=0


cnt=0
for i in range(n-1,0,-1):
    if s[i]=='L':
        cnt+=1

        if s[i-1]=='R':
            children[i]+=(cnt+1)//2
            children[i-1]+=cnt//2

    else:
        cnt=0

print(*children)