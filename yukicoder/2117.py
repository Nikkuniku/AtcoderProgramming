b0, c0 = map(int, input().split())
b1, c1 = map(int, input().split())
n = b0*b1

ans = 'NaN'
for i in range(n):
    if i % b0 == c0 % b0 and i % b1 == c1 % b1:
        ans = i
        break
print(ans)
