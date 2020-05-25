n,m=map(int,input().split())

d={}

for i in range(n):
    A,B=map(int,input().split())

    if A in d:
        d[A]+=B
    else:
        d[A]=B

l = sorted(list(d.items()),key=lambda x: x[0])

total=0
cnt=0

for i in range(len(l)):
    total+=l[i][0]*l[i][1]

    cnt+=l[i][1]

    if cnt>m:
        total -= l[i][0]*(cnt-m)
        print(total)
        exit(0) 

print(total)
