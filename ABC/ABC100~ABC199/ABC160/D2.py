n,x,y=map(int,input().split())
x,y=x-1,y-1
ans=[0]*n

for i in range(n-1):
    for j in range(i+1,n):
        d = min(abs(i-j),abs(i-x)+1+abs(y-j))

        ans[d]+=1

for k in range(1,n):
    print(ans[k])