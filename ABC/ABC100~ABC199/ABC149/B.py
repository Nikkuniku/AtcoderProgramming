A,B,K =map(int,input().split())

if A>=1 and K>0:
    tmp=A
    A=A-K
    K=K-tmp
if A<0:
    A=0

if A==0 and B>=1 and K>0:
    B=B-K

if B<0:
    B=0

print(A,B)
