N=int(input())

alls = range(1,N+1)

odds= [n for n in alls if n%2== 1] 

print(len(odds)/N)