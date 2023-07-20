def judge(n, s):
    C = s.count('1')
    # 0個なら操作不要
    if C == 0:
        return 0
    # 奇数なら不可
    if C % 2 == 1 or (s in ['110', '011']):
        return -1
    # 2より大きい偶数なら可能
    if C > 2:
        return C//2
    else:
        if s == '0110':
            return 3
        elif '11' in s:
            return 2
        else:
            return 1


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    ans.append(judge(N, S))
print(*ans, sep="\n")
