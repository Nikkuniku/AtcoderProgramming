from collections import Counter

N=int(input())

Words=[]
for i in range(N):
    Words.append(input())

c = Counter(Words)

max_value = max(c.values())

word_list=[i[0] for i in c.most_common() if i[1] == max_value]

for k in sorted(word_list):
    print(k)