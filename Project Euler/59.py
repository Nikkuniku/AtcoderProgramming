import sys
from string import ascii_lowercase, ascii_letters
from collections import Counter

f = open("./0059_cipher.txt", "r")
S = list(map(int, f.read().split(",")))
# 表示内容の出力をファイルに変更
# sys.stdout = open("0059_cipher.log", "w")
P = ascii_lowercase
letters = set(list(ascii_letters))
mod3 = [[] for _ in range(3)]
for i, v in enumerate(S):
    mod3[i % 3].append(v)
# exp
for s in ascii_lowercase:
    C = Counter()
    for a in mod3[2]:
        C[chr(a ^ ord(s))] += 1
    print(s, C.most_common()[:5])
ans = 0
password = "exp"
for i, v in enumerate(S):
    ans += S[i] ^ ord(password[i % 3])
print(ans)

# ファイルを閉じて標準出力を元に戻す
sys.stdout.close()
sys.stdout = sys.__stdout__
