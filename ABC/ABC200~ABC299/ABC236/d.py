from sys import setrecursionlimit
n = int(input())
ans = 0
a = [list(map(int, input().split())) for _ in range(2*n - 1)]

setrecursionlimit(1000000)


def dfs(s, p, score):
    '''
    s:set
        これまでに取ったもの
    p:int
        直前に取ったもの
    score:int
        現在のスコア
    '''
    # 全員組み合わせた時
    if len(s) == 2*n:
        global ans
        ans = max(ans, score)
        return
    # 長さが奇数の時
    if len(s) % 2 != 0:
        for i in range(p+1, 2*n):
            if i in s:
                continue
            score ^= a[p][i-p-1]
            s.add(i)
            dfs(s, i, score)
            s.discard(i)
            score ^= a[p][i-p-1]
    else:
        for i in range(2*n):
            if i not in s:
                break
        s.add(i)
        dfs(s, i, score)
        s.discard(i)


dfs(set(), -1, 0)
print(ans)
