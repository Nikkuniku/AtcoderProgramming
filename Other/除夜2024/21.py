S = set(list(map(int, input().split())))
T = set([1, 2, 3])
T -= S

if len(T) == 1:
    print(min(T))
else:
    print(-1)
