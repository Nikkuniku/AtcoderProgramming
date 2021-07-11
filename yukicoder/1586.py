n=int(input())
a=list(map(int,input().split()))

ans='No'
s=sum(a)
diff=0
if s%n!=0:
    print(ans)
    exit(0)

for i in range(n):
    diff += abs(s//n - a[i])

if diff%2==0:
    ans='Yes'

print(ans)