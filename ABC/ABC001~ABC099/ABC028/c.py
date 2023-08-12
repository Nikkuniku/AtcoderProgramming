import itertools
print(sorted(set([sum(c) for c in itertools.permutations(
    list(map(int, input().split())), 3)]))[::-1][2])
