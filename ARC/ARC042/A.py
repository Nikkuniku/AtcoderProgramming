n,m=map(int,input().split())

memory=[0]*n
queue=[]
for j in range(n,0,-1):
    queue.append(j)

for _ in range(m):
    i=int(input())
    queue.append(i)

queue=list(reversed(queue))

for i in queue:
    if memory[i-1]==0:
        print(i)
        memory[i-1]+=1
    else:
        continue
