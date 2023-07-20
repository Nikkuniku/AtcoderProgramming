P = list(map(int, input().split()))
ans = []
for i in range(len(P)):
    ans.append(chr(96+P[i]))
print(''.join(ans))
