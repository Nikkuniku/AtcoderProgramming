n,a,b=map(int,input().split())
score=[]
for _ in range(n):
    score.append(int(input()))

s_max=max(score)
s_min=min(score)

if s_max==s_min:
    print(-1)
    exit(0)

avg = 0
for s in score:
    avg+=s
avg/=n


p=b/(s_max-s_min)
q=a-p*avg

print(p,q)