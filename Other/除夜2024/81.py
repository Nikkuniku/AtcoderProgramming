a, b, c = map(int, input().split())
ans = "Yes"
while 1:
    b += 1
    b %= 24
    if b == a:
        ans = "No"
    if b == c:
        break
print(ans)
