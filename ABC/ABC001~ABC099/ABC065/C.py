n,m = map(int,input().split())

from math import factorial
mod =(10**9) + 7
# v_n = 1
# for i in range(1,n+1):
#     v_n*= i%mod
# v_m = 1
# for j in range(1,m+1):
#     v_m*= j%mod

v_n = factorial(n)
v_m = factorial(m)
if n==m:
    value = (v_n *v_m * 2)%mod
    print(value)

elif abs(n-m)>=2:
    print(0)

else:
    ans = (v_n * v_m)%mod
    print(ans)