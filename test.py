n=int(input())

ans=0
from itertools import permutations
p=permutations([i for i in range(n)])

nums=[0]*11
for c in p:
    cnt=0
    for j in range(n):
        if c[j]==j:
            cnt+=1
    
    nums[cnt]+=1

print(nums)