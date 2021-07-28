from sys import stdin

B,C=map(int,input().split())

if B<=0:
    a = B - C//2
    b = B + max(C-2,0)//2

    c = -B - (C-1)//2
    d = -B + (C-1)//2
else:
    a = -B - (C-1)//2
    b = -B + (C-1)//2

    c = B - C//2
    d = B + max(C-2,0)//2

ans = b + d - a - c + 2

if max(a,c)<=min(b,d):
    ans = d - a + 1 

print(ans)