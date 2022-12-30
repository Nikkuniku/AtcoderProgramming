N=int(input())
v =list(map(int,input().split()))

v = sorted(v)



values = [v[i]/(2**(N-i)) for i in range(N)]
values[0] = values[0]*2
print(sum(values))