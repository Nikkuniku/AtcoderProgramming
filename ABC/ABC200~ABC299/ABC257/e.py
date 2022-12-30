N = int(input())
C = list(map(int, input().split()))
minC = min(C)
k = -1
for i, v in enumerate(C, start=1):
    if v == minC:
        k = i
keta = N//minC
ans = []
i = 0
while keta > 0:
    for j in range(8, -1, -1):
        if (N-C[j])//minC == keta-1:
            ans.append(str(j+1))
            N -= C[j]
            break
    keta -= 1
print(''.join(ans))
