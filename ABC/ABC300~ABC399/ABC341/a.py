N = int(input())
a = [0] * N
b = [1] * (N + 1)
ans = []
while a or b:
    if b:
        ans.append(b.pop())
    if a:
        ans.append(a.pop())
print(*ans, sep="")
