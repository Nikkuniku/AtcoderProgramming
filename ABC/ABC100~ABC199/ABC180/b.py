N = int(input())
X = list(map(int, input().split()))
ans_m = 0
ans_y = 0
ans_c = 0
for x in X:
    ans_m += abs(x)
    ans_y += x**2
    ans_c = max(ans_c, abs(x))
ans_y = ans_y**(0.5)
print(ans_m)
print(ans_y)
print(ans_c)
