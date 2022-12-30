n,m,k = map(int,input().split())

import math

mod = 998244353


if k ==0:
    print(m*((m-1)**(n-1)) % mod)
else:
    print( ( m * ( ( (m-1)**(n-1) ) + k*m*(n-1) ) ) % mod)