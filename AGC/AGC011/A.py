n,c,k = map(int,input().split())

t=[]

for _ in range(n):
    t_i = int(input())

    t.append(t_i)

t = sorted(t)

bus=0
index=0
cnt=0

start =t[index]
while index<n:

    end = t[index]

    if end<=start+k:
        if cnt==c:
            bus+=1
            start=t[index]
            cnt=1
            index+=1
        else:
            cnt+=1
            index+=1
            if index==n:
                break
    else:
        bus+=1
        start=t[index]
        cnt=1
        index+=1

if cnt<=c:
    bus+=1

print(bus)


    


