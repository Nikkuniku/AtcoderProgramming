N = int(input())
if 1 <= N <= 2:
    print("O")
elif N == 3:
    print("X")
else:
    p = N % 4
    xor = 0
    for i in range(p + 1):
        xor ^= N - i
    print("O" if xor else "X")
