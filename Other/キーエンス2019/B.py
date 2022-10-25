s = input()
ans = 'NO'
for i in range(7):
    p = s[:i+1]
    q = s[-(7-(i+1)):]
    if p+q == 'keyence':
        ans = 'YES'
print(ans)
