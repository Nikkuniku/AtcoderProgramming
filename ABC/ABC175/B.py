n=int(input())
l=list(map(int,input().split()))

cnt=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            a=l[i]
            b=l[j]
            c=l[k]
                
            if(a!=b and b!=c and c!=a)and (l[i]+l[j]>l[k] and l[j]+l[k]>l[i] and l[i]+l[k]>l[j]) :
                cnt+=1

print(cnt)