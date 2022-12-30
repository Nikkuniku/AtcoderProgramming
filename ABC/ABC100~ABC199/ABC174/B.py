n,d=map(int,input().split())

cnt=0

for _ in range(n):
    x,y=map(int,input().split())

    dist =( x**2 + y**2 )**0.5

    if dist<=d:
        cnt+=1


print(cnt)