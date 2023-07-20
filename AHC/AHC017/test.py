from collections import Counter
a = list(map(int, input().split()))
C = Counter(a)
print(C)
# from math import ceil
# N, M, D, K = map(int, input().split())
# arr = [ceil(M/D) for _ in range(D)]
# tmpK = K-ceil(M/D)
# for i in range(D+1):
#     if tmpK:
#         cnt = 0
#         for j in range(min(tmpK-i, K-ceil(M/D))):
#             arr[i] += 1
#             arr[D-1-i] -= 1
#             cnt += 1
#         tmpK -= cnt
# print(arr)
# print(sum(arr))
