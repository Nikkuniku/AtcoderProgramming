N = list(map(int, input().split()))
xor = 0
for a in N:
    xor ^= a % 4
ans = "Taro" if xor else "Jiro"
print(ans)
