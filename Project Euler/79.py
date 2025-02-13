f = open("./0079_keylog.txt", "r")
S = f.read().split("\n")
S = sorted(set([int(s) for s in S]))
print(S)
usedigit = set()
for s in S:
    while s > 0:
        usedigit.add(s % 10)
        s //= 10
usedigit = list(usedigit)
