n,m  =map(int,input().split())

root=[[pow(10,9)]*n for _ in range(n) ]

for _ in range(m):
    a,b = map(int,input().split())

    root[a-1][b-1] = 0

now= 0

sirube = [0]*n

for i in range(n):

    distance=float('inf')

    for j in range(len(root)):

        if distance>root[i][j]:

            distance = root[i][j]

            sirube[j] = i

            tmp=j

    now =tmp
    
    sirube[j] = i





print(sirube)

print(*root,sep="\n")