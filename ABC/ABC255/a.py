r, c = map(int, input().split())
r -= 1
c -= 1
a = []
for _ in range(2):
    a.append(list(map(int, input().split())))

print(a[r][c])
