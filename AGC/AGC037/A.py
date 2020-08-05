s=input()

n=len(s)
if n==1:
    print(1)
    exit(0)

cnt=0
prev=s[0]
flg=0
for i in range(1,n):
    if flg==0:
        if prev==s[i]:
            flg=1
        else:
            cnt+=1
            prev=s[i]
    else:
        cnt+=1
        prev=s[i]

print(cnt+1)
    
