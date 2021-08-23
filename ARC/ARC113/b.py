a,b,c=map(int,input().split())
ans=[]
s=set()
for i in range(1,11):
    if ans and (a**i)%10 in s:
        break
    ans.append((a**i)%10)
    s.add((a**i)%10)

p=pow(b,c,len(ans))
if p==0:
    p=len(ans)-1
else:
    p-=1
print(ans[p])
