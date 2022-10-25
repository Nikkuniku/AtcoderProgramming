s = input()
t = input()
n = len(s)
m = len(t)

if n > m:
    print('No')
    exit()

ans = 'Yes'
for i in range(n):
    if s[i] != t[i]:
        print('No')
        exit()
print(ans)
