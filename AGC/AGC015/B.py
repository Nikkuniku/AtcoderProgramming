s=input()

n=len(s)

cnt=0
for i in range(n):
    if i==0:
        cnt+=n-1
        continue
    elif i==n-1:
        cnt+=n-1
        continue

    if s[i]=='U':
        cnt+=(n-1-i)
        cnt+=i*2
    else:
        cnt+=i
        cnt+=(n-1-i)*2

print(cnt)
