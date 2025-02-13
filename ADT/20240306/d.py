R, C = map(int, input().split())
V = max(abs(R - 8), abs(C - 8))
ans = "white" if V % 2 == 0 else "black"
print(ans)
