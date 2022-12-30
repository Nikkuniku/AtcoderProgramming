x,y=input().split('.')
y=int(y)
ans=x
if 0<=y<=2:
    ans+='-'
elif 7<=y<=9:
    ans+='+'
print(ans)