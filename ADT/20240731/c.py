p, q = input().split()
d = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}
a = d[p]
b = d[q]
if a > b:
    a, b = b, a
print(b - a)
