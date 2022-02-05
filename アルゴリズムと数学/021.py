n,r=map(int,input().split())
from math import factorial

ans= factorial(n)//(factorial(r)*factorial(n-r))
print(ans)