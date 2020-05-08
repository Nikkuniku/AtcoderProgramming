N,D=map(int,input().split())

r = 2*D+1
if N/r > N//r:
    print(N//r +1)
else:
    print(int(N/r))
