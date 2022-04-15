s = input()
k = int(input())
n = len(s)
substrings = set()
for i in range(n-1, -1, -1):
    p = ''
    for j in range(5):
        if i+j >= n:
            continue
        p += s[i+j]
        substrings.add(p)
substrings = list(substrings)
substrings = sorted(substrings)
print(substrings[k-1])
