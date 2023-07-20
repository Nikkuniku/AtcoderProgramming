X = set(list(map(int, input().split())))
S = {0, 1, 2}
if len(X) == 1:
    print(min(X))
else:
    print(min(S-X))
