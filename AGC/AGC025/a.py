N = int(input())
ans = 1 << 60
for a in range(1, N):
    b = N-a
    tmp = sum([int(str(a)[i]) for i in range(len(str(a)))] +
              [int(str(b)[i]) for i in range(len(str(b)))])
    ans = min(ans, tmp)
print(ans)
