from bisect import bisect_left
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ans=0
for i in range(N):
    idx=bisect_left(A,A[i]+M)
    ans=max(ans,idx-i)
print(ans)
