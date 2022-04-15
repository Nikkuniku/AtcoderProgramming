a,b=map(int,input().split())

ans='No'
if (a==1 and b==10) or(a==10 and b==1) or abs(a-b)==1:
    ans='Yes'
print(ans)