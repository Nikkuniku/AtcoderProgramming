n,x,y = map(int,input().split())

x,y = x-1,y-1

d={}
for k in range(1,n):
    d[k]=0


for i in range(n):
    for j in range(i+1,n):
     
        dist=min(abs(i-j) , abs( i - x ) + 1 + abs(y - j) ,abs( i - y ) + 1 + abs(x - j))

        d[dist]+=1

for k in range(1,n):
    print(d[k])
#BFS
# r = [[] for i in range(n)]
# for i in range(n):
#     if i==0:
#         r[i].append(i+1)
#     elif i==n-1:
#         r[i].append(n-2)
#     else:
#         r[i].append(i-1)
#         r[i].append(i+1)

# #x,yの間に道を追加
# x,y = x-1,y-1

# r[x].append(y)
# r[y].append(x)

# from collections import deque

# q = deque([0])

# dist = [-1]*n
# dist[0]=0

# ans=[]
# for p in range(n):
    
#     dist = [-1]*n
#     dist[p]=0
#     q = deque([p])

#     while q:
#         v = q.popleft()

#         for j in r[v]:
#             if dist[j]==-1:
#                 dist[j] = dist[v] + 1
#                 q.append(j)
    
#     ans.append(dist)


# d={}
# for k in range(1,n+1):
#     d[k]=0


# for i in range(n):
#     for j in range(i+1,n):
#         d[ans[i][j]]+=1

# for k in range(n-1):
#     print(d[k+1])
