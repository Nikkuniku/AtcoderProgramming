S = input()
N = len(S)
T = set()
for i in range(N):
    for j in range(i + 1, N + 1):
        T.add(S[i:j])
print(len(T))
