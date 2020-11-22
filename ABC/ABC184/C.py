r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())


if r1 ==r2 and c1 == c2:
    print(0)
    exit(0)

if (r1+c1)==(r2+c2) or (r1-c1)==(r2-c2):
    print(1)
    exit(0)

if abs(r1-r2) + abs(c1-c2) <= 3:
    print(1)
    exit(0)

if c2>c1:
    r2-=(c2-c1)
else :
    r2+=abs(c2-c1)

if abs(r2-r1)%2==0 or abs(r2-r1)<=3:
    print(2)
else:
    print(3)
