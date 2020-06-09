N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

manzoku=0


for i in range(N):
    ryori = A[i]

    manzoku+=B[ryori-1]

    if i!=0:
        if ryori-1 == ryori_pre:
            manzoku+=C[ryori_pre-1]

    ryori_pre = A[i]


print(manzoku)