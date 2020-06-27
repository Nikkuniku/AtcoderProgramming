n=int(input())
cost=[]
start=[]
fre=[]

from math import ceil

for _ in range(n-1):
    c,s,f=map(int,input().split())
    cost.append(c)
    start.append(s)
    fre.append(f)


for i in range(n):
    if i==n-1:
        print(0)
        break

    time=start[i]+cost[i]

    for j in range(i+1,n-1):
        if time>=start[j] and time%fre[j]==0:
            time+=cost[j]
        elif time>=start[j] and time%fre[j]!=0:
            time+=fre[j]*ceil(time/fre[j])-time+cost[j]
        else:
            time=start[j]+cost[j]

    print(time)

