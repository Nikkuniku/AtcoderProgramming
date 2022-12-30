N,M =map(int,input().split())
H=list(map(int,input().split()))

ALLWORK =sum(H)

if N-ALLWORK>=0:
    print(N-ALLWORK)
else:
    print('-1')