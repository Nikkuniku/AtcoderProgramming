n=int(input())
a= list(map(int,input().split()))

b=[]
for i in range(n):
    b.append(a[i]-i-1)

b=sorted(b)
if n%2==1:
    ave = b[(n-1)//2]
else:
    ave = (b[n//2] + b[(n//2)-1])//2


ans = 0
for j in range(n):
    ans += abs(b[j]-ave)

print(ans)