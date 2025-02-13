S = input()
N = len(S)
T = set()
for i in range(N):
    temp = []
    for j in range(i, N):
        temp.append(S[j])
        T.add("".join(temp))
print(len(T))
