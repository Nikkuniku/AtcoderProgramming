n = int(input())

a = list(map(int,input().split()))

d={}

for i in range(n):
    d[i+1]=a[i]


d=sorted(d.items(),key=lambda x: x[1],reverse=True)

for i in range(n):
    print(d[i][0])