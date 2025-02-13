a = int(input())
b = int(input())
ans = min((a - b) % 10, (b - a) % 10)
print(ans)
