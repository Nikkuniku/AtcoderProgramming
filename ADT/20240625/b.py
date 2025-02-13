s1 = input()
s2 = input()
c = s1.count("#") + s2.count("#")
if c > 2:
    exit(print("Yes"))
if (s1[0] == "#" and s2[1] == "#") or (s2[0] == "#" and s1[1] == "#"):
    print("No")
else:
    print("Yes")
