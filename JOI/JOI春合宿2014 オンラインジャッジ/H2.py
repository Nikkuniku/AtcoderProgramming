from collections import defaultdict
from itertools import accumulate
N = int(input())
S = input()
J = list(accumulate([0]+[1 if s == 'J' else 0 for s in S]))
O = list(accumulate([0]+[1 if s == 'O' else 0 for s in S]))
I = list(accumulate([0]+[1 if s == 'I' else 0 for s in S]))
JO = [j-o for j, o in zip(J, O)]
JI = [j-i for j, i in zip(J, I)]
d = defaultdict(list)
for i, (jo, ji) in enumerate(zip(JO, JI)):
    d[(jo, ji)].append(i)
ans = max([v[-1]-v[0] for v in d.values()])
print(ans)
