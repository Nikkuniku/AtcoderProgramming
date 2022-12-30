from collections import deque

s=deque(input())
n=len(s)

sentence=[]
for i in range(n):
    tmp=''.join(s)
    sentence.append(tmp)
    v=s.pop()
    s.appendleft(v)

sentence = sorted(sentence)

print(sentence[0])
print(sentence[-1])