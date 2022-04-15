n=int(input())
points=[[0]*(n+1) for _ in range(2)]

for i in range(n):
    c,p=map(int,input().split())
    c-=1
    points[c][i+1]=p


for j in range(n):
    points[0][j+1]+=points[0][j]
    points[1][j+1]+=points[1][j]


q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    l-=1
    ans1=points[0][r]-points[0][l]
    ans2=points[1][r]-points[1][l]
    print(ans1,ans2)