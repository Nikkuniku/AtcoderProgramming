a,b=map(int,input().split())

ans='Yes'
if 6*a<b or a>b:
    ans='No'

print(ans)