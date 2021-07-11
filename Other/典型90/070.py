n=int(input())
x=[]
y=[]

for _ in range(n):
    x_i,y_i =map(int,input().split())
    x.append(x_i)
    y.append(y_i)


x=sorted(x)
y=sorted(y)
if n%2==0:
    X=(x[(n//2)-1] + x[n//2])//2
    Y=(y[(n//2)-1] + y[n//2])//2
else:
    X=x[n//2]
    Y=y[n//2]

ans=0
for i in range(n):
    ans+=abs(x[i]-X)
    ans+=abs(y[i]-Y)

print(ans)