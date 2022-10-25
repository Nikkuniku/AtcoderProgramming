n = int(input())
a = list(map(int, input().split()))
xor = 0
for i in range(n):
    xor ^= a[i]
ans = 'First'
if xor == 0:
    ans = 'Second'
print(ans)
