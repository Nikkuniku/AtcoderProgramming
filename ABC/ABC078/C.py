n,m=map(int,input().split())

p=1/(2**m)

print(int((1900*m + 100*(n-m))/p))