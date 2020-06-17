n=int(input())

ans=[1]
i=1
s=1
while True:
    if s>=n:
        break
    i+=1
    s+=i
    ans.append(i)

dif = s-n
if dif==0:
    for i in range(len(ans)):
        print(ans[i])
    exit(0)

for i in range(len(ans)):
    if ans[i]==dif:
        continue
    print(ans[i])


