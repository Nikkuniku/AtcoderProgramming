N = input()
X = sum([int(p) for p in N])
ans = "Yes" if int(N) % X == 0 else "No"
print(ans)
