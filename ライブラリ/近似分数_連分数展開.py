def Approximate_fraction_ByContinued_Fraction(input_array: list):
    """
    連分数展開された配列から近似分数p/qを返す。

    Parameters
    ----------
    input_array:list
    """
    pn, qn = input_array[0], 1
    pn_1, qn_1 = -1, -1
    pn_2, qn_2 = -1, -1
    for i in range(1, len(input_array)):
        pn_2, qn_2 = pn_1, qn_1
        pn_1, qn_1 = pn, qn
        if i == 1:
            pn = input_array[i - 1] * input_array[i] + 1
            qn = input_array[i]
        else:
            pn = input_array[i] * pn + pn_2
            qn = input_array[i] * qn + qn_2
    return pn, qn


A = [1]
print(Approximate_fraction_ByContinued_Fraction(A))
