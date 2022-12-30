n,k=map(int,input().split())
a = list(map(int,input().split()))

#訪れた町
visited = [0]*n
visited[0]=1
root=[0]

next=a[0]-1
same=0
cnt=0
while cnt<k:
    if visited[next]==1:

        same=next

        root.append(next)

        index = root.index(same)

        break
    else:
        visited[next]=1
        root.append(next)

    next = a[next]-1
    cnt+=1

# print(visited)
# print(root)
# print(index)
if cnt==k:
    print(root[-1]+1)
    exit(0)

roops=len(root) - index -1 

if roops!=0:
    moves = index + ( (k-index)%roops )
else:
    moves= index

now=0

for i in range(moves):
    now=a[now]-1

print(now+1)


