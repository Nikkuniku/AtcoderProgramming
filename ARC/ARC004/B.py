n=int(input())
edges=[]
for _ in range(n):
    edges.append(int(input()))

edges=sorted(edges,reverse=True)

print(sum(edges))
if n==1:
    print(edges[0])
elif n==2:
    print(edges[0]-edges[1])
else:
    if 2*edges[0]>sum(edges):
        print(2*edges[0]-sum(edges))
    else:
        print(0)