t=int(input())
n=int(input())

num=[0]*(11*t)
for _ in range(n):
    l,r=map(int,input().split())
    num[l*10]+=1
    num[r*10]-=1

for i in range(10*t-1):
    num[i+1]+=num[i]

for j in range(t):
    p=j*10+5
    print(num[p])