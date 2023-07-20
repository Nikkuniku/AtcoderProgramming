N = int(input())
people = []
Age = []
for _ in range(N):
    s, a = input().split()
    a = int(a)
    people.append(s)
    Age.append(a)
idx = Age.index(min(Age))
ans = []
for i in range(N):
    ans.append(people[(idx+i) % N])
print(*ans, sep="\n")
