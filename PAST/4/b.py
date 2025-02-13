from math import floor

X, Y = map(int, input().split())
if Y == 0:
    exit(print("ERROR"))
ans = floor(X / Y * 100) / 100
print("{:.2f}".format(ans))
