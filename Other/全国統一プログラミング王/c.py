from dis import dis


n = int(input())
dish = []
for _ in range(n):
    a, b = map(int, input().split())
    s = a-(-b)
    dish.append((a, b, s))
dish.sort(reverse=True, key=lambda x: x[2])
if n % 2 == 0:
    p = n//2 + 1
else:
    p = n//2
t = 0
a = 0
for i in range(n):
    if i <= p:
        t += dish[i][0]
    else:
        a += dish[i][1]

ans = t-a
print(ans)
