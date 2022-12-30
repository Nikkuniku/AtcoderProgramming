n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

label=[-1]*n

l=1
for i in range(n):
    if label[i]==-1:
        label[i]=l

        while True:
            j=p[i]
            if label[j-1]==-1:
                label[j-1]=l
            else:
                break

            i=j-1
        
        l+=1

l_m=max(label)

can=[0]*l_m
num=[0]*l_m
for i in range(n):
    j=label[i]-1

    num[j]+=1
for i in range(n):
    j=label[i]-1

    can[j]+=c[i]

print(can)
print(num)