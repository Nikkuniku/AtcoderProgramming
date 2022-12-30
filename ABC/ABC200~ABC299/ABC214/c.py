n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=t.copy()


for i in range(n):
   if i==0:
       ans[i]=min(ans[-1]+s[-1],ans[i]) 
   else:
       ans[i]=min(ans[i-1]+s[i-1],ans[i])

for i in range(n):
   if i==0:
       ans[i]=min(ans[-1]+s[-1],ans[i]) 
   else:
       ans[i]=min(ans[i-1]+s[i-1],ans[i])
       
for j in range(n):
    print(ans[j])