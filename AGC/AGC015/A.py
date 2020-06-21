n,a,b=map(int,input().split())


ans=0
if n==1 and a!=b:
    ans=0
elif a==b:
    ans=1
elif a>b:
    ans=0
else:
    ans= (n-2)*(b-a)

print(ans)
    

