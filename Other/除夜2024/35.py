N = int(input()) - 1
if N == 0:
    exit(print(0))
digit = []
while N > 0:
    digit.append(N % 5)
    N //= 5
mapping = [0, 2, 4, 6, 8]
ans = [mapping[digit[::-1][i]] for i in range(len(digit))]
print(*ans, sep="")
