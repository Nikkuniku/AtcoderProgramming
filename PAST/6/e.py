from collections import deque

N = int(input())
S = input()
q = deque()
for i, s in enumerate(S):
    if s == "L":
        q.appendleft(i + 1)
    elif s == "R":
        q.append(i + 1)
    elif s == "A":
        if q:
            print(q.popleft())
        else:
            print("ERROR")
    elif s == "B":
        if len(q) > 1:
            a = q.popleft()
            b = q.popleft()
            print(b)
            q.appendleft(a)
        else:
            print("ERROR")
    elif s == "C":
        if len(q) > 2:
            a = q.popleft()
            b = q.popleft()
            c = q.popleft()
            print(c)
            q.appendleft(b)
            q.appendleft(a)
        else:
            print("ERROR")
    elif s == "D":
        if q:
            print(q.pop())
        else:
            print("ERROR")
    elif s == "E":
        if len(q) > 1:
            a = q.pop()
            b = q.pop()
            print(b)
            q.append(a)
        else:
            print("ERROR")
    elif s == "F":
        if len(q) > 2:
            a = q.pop()
            b = q.pop()
            c = q.pop()
            print(c)
            q.append(b)
            q.append(a)
        else:
            print("ERROR")
