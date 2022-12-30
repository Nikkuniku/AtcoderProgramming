n,k=map(int,input().split())
p=list(map(int,input().split()))

p=sorted(p)

print(sum(p[:k]))