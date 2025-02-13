N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    i = P.index(a)
    j = P.index(b)
    if i < j:
        print(a)
    else:
        print(b)
