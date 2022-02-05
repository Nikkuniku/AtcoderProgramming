n=int(input())

p=n+1
ans='First'
if p&(p-1)==0:
    ans='Second'
print(ans)