a,b,c = map(int,input().split())
k=int(input())

cnt=0
while b<=a:
    b*=2
    cnt+=1

while c<=b:
    c*=2
    cnt+=1

if cnt<=k:
    print('Yes')
else:
    print('No')

    