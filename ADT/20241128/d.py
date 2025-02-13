N = int(input())
S = [list(input()) for _ in range(N)]
Won = []
for i in range(N):
    temp = 0
    for j in range(N):
        if i == j:
            continue
        if S[i][j] == "o":
            temp += 1
    Won.append(temp)
A = [(i + 1, Won[i]) for i in range(N)]
A.sort(key=lambda x: x[0])
A.sort(key=lambda x: x[1], reverse=True)
print(*[a[0] for a in A])
