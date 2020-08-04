d,n=map(int,input().split())
# # nは1<=n<=100

s=1
if d==1:
    s=100
elif d==2:
    s=10000

if s==1:
    ans=[i for i in range(1,100)]
    ans.append(101)
elif s==100:
    ans=[100*i for i in range(1,100)]
    ans.append(10100)

else:
    ans=[10000*i for i in range(1,100)]
    ans.append(1010000)

print(ans[n-1])