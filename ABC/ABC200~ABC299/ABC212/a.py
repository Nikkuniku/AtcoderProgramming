a,b=map(int,input().split())
ans='Alloy'
if a>0 and b==0:
    ans='Gold'
elif a==0 and b>0:
    ans='Silver'

print(ans)