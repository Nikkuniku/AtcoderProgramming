n = int(input())
l = list(map(int,input().split()))

longest =max(l)

index = l.index(longest)

total = 0
for i in range(n):
    if i!=index:
        total+=l[i]

if longest<total:
    print('Yes')
else:
    print('No')