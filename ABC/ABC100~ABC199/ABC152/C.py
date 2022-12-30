N=int(input())
Nums = list(map(int,input().split()))

min_value=Nums[0]

cnt=0

for i in range(N):
    min_value = min(min_value,Nums[i])
    
    if Nums[i]<=min_value:
        cnt+=1
    
    

print(cnt)