s=list(input().split())
t=list(input().split())

cnt=0
for i in range(3):
    if s[i]!=t[i]:
        cnt+=1

ans='Yes'
if cnt==2:
    ans='No'
print(ans)