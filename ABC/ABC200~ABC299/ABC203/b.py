n,k=map(int,input().split())

rooms=[]

for i in range(n):
    for j in range(k):
        r = str(i+1)+'0'+str(j+1)
        r =int(r)
        rooms.append(r)

print(sum(rooms))