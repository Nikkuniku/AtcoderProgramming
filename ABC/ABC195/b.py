a,b,w=map(int,input().split())

ans1=10**10
ans2=0
for i in range(1,10**7):
    if a<=(1000*w)/i<=b:
        ans1=min(ans1,i)
        ans2=max(ans2,i)

if ans1==10000000000 or ans2==0:
    print('UNSATISFIABLE')
    exit(0)
print(ans1,ans2)