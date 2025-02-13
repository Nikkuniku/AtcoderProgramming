def RLE(S: list) -> list:
    """
    入力をランレングス圧縮したリストを返す.
    [(value1,length1),(value2,length2),...]

    Parameters
    -----------
    S:list

    Examples
    --------
    >>> RLE('aaabbc')
    [('a', 3), ('b', 2), ('c', 1)]
    """
    from more_itertools import run_length

    res = list(run_length.encode(S))
    return res


N = int(input())
S = input()
if S == "/":
    exit(print("Yes"))
if N % 2 == 0:
    exit(print("No"))
if S[N // 2] != "/":
    exit(print("No"))
R = RLE(S)
ans = "No"
if len(R) == 3:
    if (
        R[0][0] == "1"
        and R[0][1] == N // 2
        and R[1][0] == "/"
        and R[1][1] == 1
        and R[2][0] == "2"
    ):
        ans = "Yes"
print(ans)
