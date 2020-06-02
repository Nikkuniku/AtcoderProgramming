n=int(input())
p=list(map(int,input().split()))

cnt=0
flg=0
for i in range(n-1):
    if p[i]==i+1 and p[i+1]==i+2:
        cnt+=1
        flg=1
    elif flg==1 and p[i]==i+1 and p[i+1]!=i+2:
         flg=0
    elif flg==0 and p[i]==i+1 and p[i+1]!=i+2:
        cnt+=1

if n>=3:
    if p[n-2]!=n-1 and p[n-1]==n:
        cnt+=1

print(cnt)
