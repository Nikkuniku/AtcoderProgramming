N = int(input())
S = input()
T = set()
for i in range(N):
    T.add(S[i])
    if len(T) == 3:
        break
print(i+1)
