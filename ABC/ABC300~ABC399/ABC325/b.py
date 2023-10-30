N=int(input())
A=[0]*24
for _ in range(N):
    W,X=map(int,input().split())
    t=(9+X)%24
    for _ in range(9):
        A[t]+=W
        t+=1
        t%=24
print(max(A))