N,Q=map(int,input().split())
X,Y=[],[]
for _ in range(N):
    x,y=map(int,input().split())
    X.append(x+y)
    Y.append(x-y)

x_max=max(X)
x_min=min(X)
y_max=max(Y)
y_min=min(Y)
for _ in range(Q):
    q=int(input())-1
    a1 = max(x_max-X[q],X[q]-x_min)
    a2 = max(y_max-Y[q],Y[q]-y_min)
    ans = max(a1,a2)

    print(ans)