S = input()
ans = 'Yes'
for i in range(len(S)):
    if i % 2 == 0 and S[i].isupper():
        ans = 'No'
    elif i % 2 != 0 and S[i].islower():
        ans = 'No'
print(ans)
