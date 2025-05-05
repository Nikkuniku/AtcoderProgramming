N = int(input())
status = False
ans = 0
for _ in range(N):
    S = input()
    if S == "login":
        status = True
    elif S == "logout":
        status = False
    elif S == "public":
        pass
    elif S == "private":
        if not status:
            ans += 1
print(ans)
