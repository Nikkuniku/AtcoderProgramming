S = input()
res = []
for i in range(1, 350):
    if i == 316:
        continue
    tmp = "ABC" + str(i).zfill(3)
    res.append(tmp)
ans = "No"
if S in res:
    ans = "Yes"
print(ans)
