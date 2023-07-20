T = int(input())


def judge(N, K, S):
    p = (N+K) % (2*N)
    A = S
    B = S[::-1]
    if p > N:
        tmp = []
        tmp2 = []
        for i in range(p-N):
            tmp.append(A[i])
            tmp2.append(B[i])
        A += ''.join(tmp[::-1])
        B += ''.join(tmp2[::-1])
    else:
        cnt = len(set(list(S)))
        if cnt == 1:
            return True
        else:
            return False
    Flg = True
    for i in range(len(A)//2):
        if A[i] != A[len(A)-1-i]:
            Flg = False
        if B[i] != B[len(B)-1-i]:
            Flg = False
    if Flg:
        return True
    else:
        return False


ans = []
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    res = 'No'
    if judge(N, K, S):
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
