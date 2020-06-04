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

if len(Keys)==1 and k>1 and values[0]%2==1:
    print(values[0])
    exit(0)

if Keys[0]==Keys[-1] and values[0] + values[-1] ==2 and k>1:
    cnt+=(k-1)


for i in values:
    if i>1:
        cnt += k*(i//2)
    


print(cnt)