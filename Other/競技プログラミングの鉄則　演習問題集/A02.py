n, x = map(int, input().split())
a = set(list(map(int, input().split())))

if x in a:
    print('Yes')
else:
    print('No')
