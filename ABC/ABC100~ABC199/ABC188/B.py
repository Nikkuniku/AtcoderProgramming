n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

ans=0

for i in range(n):
    p=a[i]*b[i]
    ans+=p
if ans==0:
    print('Yes')
else:
    print('No')