N, K = map(int, input().split())
A = list(map(int, input().split()))
from itertools import accumulate

if K > 0:
    A.sort()
    print("Yes")
    print(*A)
else:
    A.sort(reverse=True)
    B = list(accumulate(A))
    if B[-1] < K:
        print("No")
    else:
        print("Yes")
        print(*A)
