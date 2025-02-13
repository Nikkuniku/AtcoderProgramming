from itertools import permutations

N = int(input())
S = input()
P = list(permutations(list(S)))

for p in P:
    tmp = "".join(p)
    if tmp != S and tmp != S[::-1]:
        exit(print(tmp))
print("None")
