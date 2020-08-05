n=int(input())
a=list(map(int,input().split()))

pair=[0]*n

cnt=0
for i in range(n):
    if pair[i]==0:
        if a[a[i]-1]==i+1:
            cnt+=1
            pair[a[i]-1]=1

print(cnt)