H,N=map(int,input().split())
Attacks =list(map(int,input().split()))

Damages =sum(Attacks)

if H<=Damages:
    print('Yes')
else:
    print('No')