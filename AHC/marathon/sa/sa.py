# -+- coding: utf-8 -*-
from turtle import color
import numpy as np
from matplotlib import pyplot as plt
import random  # ランダムモジュール
import math


def annealingoptimize(T=100000, cool=0.99, step=0.1):
    xs = []
    ys = []
    # ランダムな値で初期化
    vec = random.randint(-2, 2)
    # vec = -2

    while T > 0.0001:
        # 変更する変数を一つ選ぶ。
        # 今回の場合は1次元なので選ぶ必要がない。
        # i = random.randint(0, dimmension-1)

        # 変数の値を増加させるか、減少させるかを決定する。
        dir = random.random()
        dir = (dir - 0.5) * step

        # 変数の値を変更する。
        newvec = vec + dir

        # 変更前と変更後のコストを計算する。
        newcost = costf(newvec)
        cost = costf(vec)

        # 温度から確率を定義する。
        p = pow(math.e, -abs(newcost - cost) / T)

        # 変更後のコストが小さければ採用する。
        # コストが大きい場合は確率的に採用する。
        if(newcost > cost or random.random() < p):
            # if(random.random() < p):
            vec = newvec
        xs.append(vec)
        ys.append(costf(vec))
        # 温度を下げる
        T = T * cool

    return vec, xs, ys


def costf(x):
    return ((-3)*(x**4)) + (3*(x**3)) + (10*(x**2))-(10*x)+15


ans, xs, ys = annealingoptimize()
X = np.linspace(-2, 2, 100)
plt.plot(X, costf(X))
plt.scatter(xs, ys, color='orange')
plt.xlim(-3, 3)
plt.ylim(-30, 30)
print(ans)
print(costf(ans))
plt.scatter([ans], [costf(ans)], color='red')
plt.show()
