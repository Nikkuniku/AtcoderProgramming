h,w,x,y=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))


ans =-3

x,y=x-1,y-1

for up in range(h):
    if x-up >=0 and s[x-up][y]=='.':
        ans+=1
    else:
        break

for down in range(h):
    if x+down <=h-1 and s[x+down][y]=='.':
        ans+=1
    else:
        break

for right in range(w):
    if y+right <=w-1 and s[x][y+right]=='.':
        ans+=1
    else:
        break

for left in range(w):
    if y-left >=0 and s[x][y-left]=='.':
        ans+=1
    else:
        break

print(ans)