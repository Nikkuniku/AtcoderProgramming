def genrandomsequence(n, a, b):
    import random
    re = []
    for i in range(n):
        re.append(random.randint(a, b))
    return re


n = int(input())
print(genrandomsequence(n, 1, 100))
