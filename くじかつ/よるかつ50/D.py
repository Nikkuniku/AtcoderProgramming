n=int(input())
a= list(map(int,input().split()))

s= sum(a)

s_1 = sum([a[i] for i in range(n) if i%2==1])

x_1 = s-2*s_1

ans = [x_1]

for i in range(n-1):
    x = 2*a[i] - ans[-1]
    ans .append(x)

print(*ans)