from functools import cache


@cache
def rec(k, N):
    if 2 * k > N or 2 * k + 1 > N:
        return False
    # 勝ち：True
    # 負け：False
    if not rec(2 * k, N):
        return True
    if not rec(2 * k + 1, N):
        return True
    return False


N = int(input())
res = rec(1, N)
print(res)
