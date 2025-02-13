R, G, B = map(int, input().split())
A = [R, G]
C = input()
if C == "Red":
    A = [G, B]
elif C == "Green":
    A = [R, B]
print(min(A))
