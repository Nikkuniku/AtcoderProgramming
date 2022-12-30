n=int(input())
a=list(map(int,input().split()))

s=sum(a)

if s%n!=0:
    print(-1)
    exit(0)

flg=0
for j in range(n):
    if a!=s/n:
        flg+=1
if flg==0:
    print(0)
    exit(0)

p=s//n

j=0
cnt=0
s_i=0
k=0
for i in range(n):
    s_i+=a[i]
    j=i+1
    if s_i/(j-k)==p:
        cnt+=i-k
        s_i=0
        k=j

print(cnt)
