from heapq import nsmallest


n=int(input())
a=list(map(int,input().split()))
nums=[0]*2001
for i in range(n):
    nums[a[i]]=1

ans=-1
for j in range(len(nums)):
    if nums[j]==0:
        ans=j
        break
print(ans)