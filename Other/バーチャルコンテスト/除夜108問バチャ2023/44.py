N = int(input())
A = set(list(map(int, input().split())))
for i in range(2002):
    if i not in A:
        print(i)
        break
