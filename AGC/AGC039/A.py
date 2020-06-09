s = input()
k = int(input())

from itertools import groupby

n=len(s)
cnt =0

gp = groupby(s)

Keys=[]
values=[]
for key,value in gp:
    Keys.append(key)
    values.append(len(list(value)))

if len(Keys)==1:
    print(values[0]*k//2)
    exit(0)

if k==1:
    for i in values:
        cnt+=i//2
    print(cnt)
    exit(0)
    
if k>=2:
    if Keys[0]==Keys[-1]:
        values2=list(reversed(values))

        m=len(values)

        for i in range(m-1):
            if values[i]>=2:
                cnt+=values[i]//2
            if values2[i]>=2:
                cnt+=values2[i]//2
        
        cnt+= (k-1) * ((values[0]+values[-1])//2)

        for j in range(m):
            if j==0 or j==m-1:
                continue
            else:
                cnt+= (k-2)*(values[j]//2)

        print(cnt)
        exit(0)

for i in values:
    if i>1:
        cnt += k*(i//2)


print(cnt)
