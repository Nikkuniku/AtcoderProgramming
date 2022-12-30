S,T=input().split()
A,B =map(int,input().split())
U=input()

d={}
d[S]=A
d[T]=B

if U==S:
    d[S]-=1
else:
    d[T]-=1

print(d[S],d[T])