n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range(n):
    c.append((i+1, a[i], b[i], a[i]+b[i]))
ans = []
# math
c.sort(key=lambda x: x[0])
c.sort(key=lambda x: x[1], reverse=True)
ans += c[:x]
c = c[x:]
# english
c.sort(key=lambda x: x[0])
c.sort(key=lambda x: x[2], reverse=True)
ans += c[:y]
c = c[y:]
# all
c.sort(key=lambda x: x[0])
c.sort(key=lambda x: x[3], reverse=True)
ans += c[:z]
ans.sort()
for p in ans:
    print(p[0])
