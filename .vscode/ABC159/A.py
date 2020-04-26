N,M = map(int,input().split())

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def ans(N,M):
    if N>=2 and M<2:
        return combinations_count(N,2)
    elif N<2 and M>=2:
        return combinations_count(M,2)
    elif N<2 and M<2:
        return 0
    else:
        return combinations_count(N,2) + combinations_count(M,2) 


print(ans(N,M))
