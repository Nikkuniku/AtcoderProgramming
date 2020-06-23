t=int(input())
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

if n<m:
    print('no')
    exit(0)


sold=[0]*n
for i in range(m):

    for j in range(n):
        if a[j]<=b[i] and b[i]<=a[j]+t and sold[j]==0:
            sold[j]=1
            break

if sum(sold)==m:
    print('yes')
else:
    print('no')
