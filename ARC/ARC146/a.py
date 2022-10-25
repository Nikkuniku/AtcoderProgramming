from itertools import permutations
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
p = permutations(a[:3])
answer = 0
for c in p:
    tmp = ''
    for i in c:
        tmp += str(i)
    answer = max(answer, int(tmp))
print(answer)
