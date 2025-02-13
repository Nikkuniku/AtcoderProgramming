N = int(input())
pat1 = "H,D,C,S".split(",")
pat2 = "A,2,3,4,5,6,7,8,9,T,J,Q,K".split(",")
seen = set()
ans = "Yes"
for _ in range(N):
    S = input()
    if S[0] not in pat1 or S[1] not in pat2:
        ans = "No"
    if S in seen:
        ans = "No"
    seen.add(S)
print(ans)
