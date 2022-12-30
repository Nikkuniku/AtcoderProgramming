N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

cnt=0
for i in range(N):
    if B[i] >= A[i] + A[i+1]:
        cnt +=A[i] + A[i+1]
        A[i+1]=0
    
    elif B[i] < A[i] + A[i+1] and B[i] >= A[i] :
        
        A[i+1] -= B[i]-A[i]

        cnt += A[i] + (B[i]-A[i]) 

    elif B[i] < A[i] + A[i+1] and B[i] < A[i]:
        cnt +=B[i]

print(cnt)
