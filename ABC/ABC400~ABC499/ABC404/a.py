from string import ascii_lowercase

S = input()
for s in ascii_lowercase:
    if s not in S:
        exit(print(s))
