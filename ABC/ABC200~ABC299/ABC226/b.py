n=int(input())
ans=set()

for _ in range(n):
    a=tuple(map(int,input().split()))
    ans.add(a)

print(len(ans))