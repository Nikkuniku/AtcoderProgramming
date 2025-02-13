from string import ascii_lowercase

N = int(input())
S = input()
mapping_from = mapping_to = ascii_lowercase
Q = int(input())
for _ in range(Q):
    c, d = input().split()
    mapping_to = mapping_to.replace(c, d)
ans = S.translate(str.maketrans(mapping_from, mapping_to))
print(ans)
