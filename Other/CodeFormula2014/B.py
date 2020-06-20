n=list(input())

n=list(reversed(n))
ans_o=0
ans_e=0

for i in range(len(n)):
    if i%2==0:
        ans_e+=int(n[i])
    else:
        ans_o+=int(n[i])

print(ans_o,ans_e)
