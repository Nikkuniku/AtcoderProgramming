N, Q = map(int, input().split())
T = list(map(int, input().split()))
Tooth = [1] * N
for t in T:
    if Tooth[t - 1] == 1:
        Tooth[t - 1] = 0
    else:
        Tooth[t - 1] = 1
print(sum(Tooth))
