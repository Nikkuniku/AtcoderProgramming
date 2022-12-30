n, x = map(int, input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = []
for i in range(26):
    for _ in range(n):
        s.append(alphabet[i])
print(s[x-1])
