n = int(input())

ans = -1
for a in range(1, 1000):
    for b in range(1, 1000):
        if pow(3, a)+pow(5, b) == n:
            print(a, b)
            exit(0)
print(ans)
