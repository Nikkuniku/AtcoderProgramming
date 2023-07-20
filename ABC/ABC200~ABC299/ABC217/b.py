S = set(list('ABC,ARC,AGC,AHC'.split(',')))
for _ in range(3):
    s = input()
    S.discard(s)
print(min(S))
