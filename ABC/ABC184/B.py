n,x=map(int,input().split())
s=input()


score = x
for i in range(n):
    if s[i]=='o':
        score+=1
    elif s[i]=='x':
        if score==0:
            continue
        else:
            score-=1

print(score)