s=input()

r3=s.count('RRR')
if r3==1:
    print(3)
    exit(0)
r2=s.count('RR')

if r2==1:
    print(2)
    exit(0)

r=s.count('R')

if r>=1:
    print(1)
else:
    print(0)
