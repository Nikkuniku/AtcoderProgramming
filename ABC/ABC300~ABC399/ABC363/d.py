N = int(input())
res = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
if N <= len(res):
    exit(print(res[N - 1]))
k = 1
cnt = len(res)
while 1:
    tmp = pow(10, k + 1) - pow(10, k)
    if cnt + tmp >= N:
        a = pow(10, k) + (N - cnt - 1)
        ans = list(str(a))[:-1] + list(str(a))[::-1]
        exit(print(*ans, sep=""))
    cnt += tmp
    if cnt + tmp >= N:
        a = pow(10, k) + (N - cnt - 1)
        ans = list(str(a)) + list(str(a))[::-1]
        exit(print(*ans, sep=""))
    cnt += tmp
    k += 1
