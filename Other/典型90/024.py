n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
total_abs = 0
for i in range(n):
    total_abs+=abs(a[i]-b[i])

ans='No'

if total_abs%2==0:
    if k>=total_abs and k%2==0:
        ans='Yes'
else:
    if k>=total_abs and k%2==1:
        ans='Yes'

print(ans)
