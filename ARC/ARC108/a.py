S, P = map(int, input().split())

for n in range(1, int(P**0.5)+1):
    if P % n == 0:
        m = P//n
        if n+m == S:
            print('Yes')
            exit(0)
print('No')
