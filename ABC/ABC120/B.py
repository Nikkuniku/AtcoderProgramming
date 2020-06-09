a,b,k = map(int,input().split())


cd=[]
for i in range(1,max(a,b)+1):
    if a%i ==0 and b%i ==0:
        cd.append(i)


cd = sorted(cd,reverse=True)
print(cd[k-1])

