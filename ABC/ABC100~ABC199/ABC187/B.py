n=int(input())

xy=[]
for _ in range(n):
    x,y=map(int,input().split())
    xy.append([x,y])

ans=0
for i in range(n):
    for j in range(n):
        if j>i:
            a=xy[i]
            b=xy[j]

            p=(b[1]-a[1])/(b[0]-a[0])

            if -1<=p<=1:
                ans+=1

print(ans)