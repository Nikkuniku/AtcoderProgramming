from string import ascii_lowercase

S = input()
ans = "None"
for x in ascii_lowercase:
    if x not in S:
        ans = x
        break
print(ans)
