n=int(input())
a=list(map(int,input().split()))

A=max(a)

def min_factor(k):
    d=[]
    for i in range(k+1):
        d.append(i)

    i=2
    while i*i<=k:
        if d[i]==i:
            j=i*i
            while j<=k:
                if d[j]==j:
                    d[j]=i
                j+=i
        i+=1
    
    return d

d=min_factor(A)
dic = {}

for i in range(n):
    tmp=a[i]
    while tmp!=1:
        tmp/=d[tmp]
        if tmp in dic:
            dic[tmp]+=1
        else:
            dic[tmp]=1
        
for _,v in dic.items():
    if v!=1:
        ans=''

print(d)