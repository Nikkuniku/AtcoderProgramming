S = input()
q = []
for s in S:
    q.append(s)
    if len(q) > 1:
        if q[-2] == "[" and q[-1] == "]":
            q.pop()
            q.pop()
        elif q[-2] == "(" and q[-1] == ")":
            q.pop()
            q.pop()
        elif q[-2] == "<" and q[-1] == ">":
            q.pop()
            q.pop()
if q:
    print("No")
else:
    print("Yes")
