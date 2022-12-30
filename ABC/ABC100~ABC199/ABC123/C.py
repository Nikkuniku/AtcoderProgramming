n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

now = [n,0,0,0,0,0]

from math import ceil

# i1 = ceil(n/a)
# now[0] = n - i1*a if n - i1*a >=0 else 0
# now[1] = a*(i1-1) - b*(i1-2) if a*(i1-1) - b*(i1-2) >=0 else 0
# now[2] = b*(i1-2) - c*(i1-3) if b*(i1-2) - c*(i1-3) >=0 else 0
# now[3] = c*(i1-3) - d*(i1-4) if c*(i1-3) - d*(i1-4) >=0 else 0
# now[4] = d*(i1-4) - e*(i1-5) if d*(i1-4) - e*(i1-5) >=0  else 0
# now[5] = e*(i1-5) if e*(i1-5) >=0 else 0

k = ceil(n/ min(a,b,c,d,e)) +4

print(k)