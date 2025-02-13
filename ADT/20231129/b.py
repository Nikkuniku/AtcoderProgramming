N = int(input())
S = input()
if S.count("T") > S.count("A"):
    ans = "T"
elif S.count("T") < S.count("A"):
    ans = "A"
else:
    P = S.count("T")
    t = 0
    a = 0
    for v in S:
        if v == "T":
            t += 1
        else:
            a += 1
        if t == P:
            ans = "T"
            break
        if a == P:
            ans = "A"
            break
print(ans)
