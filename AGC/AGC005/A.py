x=input()
n=len(x)

t=0
cnt=0
for i in range(n-1,-1,-1):
    if x[i]=='T':
        t+=1
    elif t>0 and x[i]=='S':
        cnt+=1
        t-=1

print(n-2*cnt)