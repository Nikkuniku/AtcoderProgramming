n=int(input())
a=list(map(int,input().split()))
d={}
for i in range(n):
    d[a[i]]=i+1
a=sorted(a,reverse=True)
print(d[a[1]])