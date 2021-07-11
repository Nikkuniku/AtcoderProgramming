import math

n=int(input())

l = list(range(1,n+1))

ans=1

# 2数を受け取って最小公倍数を返す関数
def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)


for i in range(len(l)):
    ans = lcm(ans,l[i])

print(ans)