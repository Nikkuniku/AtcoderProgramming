arr=[]
for _ in range(20):
    p=list(map(int,input().split()))
    arr.append(p)

print(arr)    

ans=0
for i in range(20):
    for j in range(20):
        if i<=16:
            tmp = arr[i][j]*arr[i+1][j]*arr[i+2][j]*arr[i+3][j]
            ans=max(ans,tmp)
            if 3<=j:
                tmp = arr[i][j]*arr[i+1][j-1]*arr[i+2][j-2]*arr[i+3][j-3]
                ans=max(ans,tmp)
            if j<=16:
                tmp = arr[i][j]*arr[i+1][j+1]*arr[i+2][j+2]*arr[i+3][j+3]
                ans=max(ans,tmp)

        if j<=16:
            tmp =arr[i][j]*arr[i][j+1]*arr[i][j+2]*arr[i][j+3]
            ans=max(ans,tmp)

print(ans)
