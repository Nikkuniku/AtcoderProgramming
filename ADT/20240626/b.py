n = int(input())
k = 0
while pow(2, k) <= n * n:
    k += 1
if n >= k:
    print("Yes")
else:
    print("No")
