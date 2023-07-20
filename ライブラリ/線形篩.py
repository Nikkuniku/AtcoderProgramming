def LinearSieve(n: int) -> list:
    '''
    2以上の整数n => 各数の最小素因数lpfの配列

    Parameters
    ----------
    n:int
    '''
    prime_list = []
    lpf = [1]*(n+1)
    for d in range(2, n+1):
        if lpf[d] == 1:
            lpf[d] = d
            prime_list.append(d)
        for p in prime_list:
            if p*d > n or p > lpf[d]:
                break
            lpf[p*d] = p
    return lpf


print(LinearSieve(2000000))
