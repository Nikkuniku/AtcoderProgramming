n=int(input())
a=list(map(int,input().split()))


s=[0]

for i in range(n):
    s.append(s[-1]+a[i])

place=s.copy()

for i in range(1,len(s)):
    place[i]+=place[i-1]

move=[s[0]]
for i in range(len(a)):
    move.append(max(move[i],s[i]+a[i]))

for j in range(len(move)-1):
    place[j]+=move[j]

print(max(place))