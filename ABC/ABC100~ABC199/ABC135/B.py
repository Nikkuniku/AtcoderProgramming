N=int(input())
p =list(map(int,input().split()))

flg=0
for i in range(N):
    if p[i]!=i+1:
        flg+=1

if flg==0 or flg==2:
    print('YES')
else:
    print('NO')

