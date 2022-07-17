a, b, c, d = map(int, input().split())
cookies = [0, 0, a, b, c, d]
s = sum(cookies)

ans = 'No'
for i in range(4):
    for j in range(i+1, 5):
        for k in range(j+1, 6):
            p = cookies[i]+cookies[j]+cookies[k]
            if s-p == p:
                ans = 'Yes'
                break
print(ans)
