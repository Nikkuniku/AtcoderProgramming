T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = [input() for _ in range(3)]
    ans.append(('0'*N) + ('1')+('0')*N)
print(*ans, sep="\n")
