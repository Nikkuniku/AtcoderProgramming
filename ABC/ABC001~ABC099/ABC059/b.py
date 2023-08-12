A = input().zfill(102)
B = input().zfill(102)
ans = 'GREATER'
for i in range(len(A)):
    a = int(A[i])
    b = int(B[i])
    if a < b:
        ans = 'LESS'
        break
    elif a > b:
        break
else:
    ans = 'EQUAL'
print(ans)
