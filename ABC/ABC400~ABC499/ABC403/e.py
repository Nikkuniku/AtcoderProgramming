from sys import setrecursionlimit

setrecursionlimit(10**8)
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        n = self.size = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self.a = [
            a[n * i // num_bucket : n * (i + 1) // num_bucket]
            for i in range(num_bucket)
        ]

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _position(self, x: T) -> tuple[list[T], int, int]:
        "return the bucket, index of the bucket and position in which x should be. self must not be empty."
        for i, a in enumerate(self.a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a, b, i = self._position(x)
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b : b + 1] = [a[:mid], a[mid:]]

    def _pop(self, a: list[T], b: int, i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            del self.a[b]
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x: T) -> T | None:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> T | None:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> T | None:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> T | None:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class Trie:
    def __init__(self):
        from collections import defaultdict

        self.nodes = []
        self.next = []
        self.accept = []
        self.c = []
        self.common = []
        self.base = ord("a")
        self.charsize = 26  # 英字分
        # root
        self.nodes.append(0)
        self.next.append(defaultdict(lambda: -1))
        self.accept.append([])
        self.c.append(-1)
        self.common.append(0)

    def insert_word(self, word: str, word_id: int):
        from collections import defaultdict

        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                next_id = len(self.nodes)
                self.nodes.append(next_id)
                self.next.append(defaultdict(lambda: -1))
                self.accept.append([])
                self.c.append(c)
                self.common.append(0)
                self.next[node_id][c] = next_id
            self.common[node_id] += 1
            node_id = next_id
        self.common[node_id] += 1
        self.accept[node_id].append(word_id)

    def insert(self, word: str):
        self.insert_word(word, self.common[0])

    def search(self, word: str, prefix: bool = False):
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return False
            node_id = next_id
        return True if prefix else len(self.accept[node_id]) > 0

    def erase(self, word: str):
        # 見つからない場合はFalseを返す
        if not self.search(word):
            return False
        # 上からたどっていって、self.commonを削除する
        # self.commonが0の時はnextも削除する
        # self.cは-1にしておく
        # 文字列の最後ではacceptからpopする
        node_id = 0
        history = []
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            history.append((node_id, c))
            node_id = next_id
        self.accept[node_id].pop()
        self.common[node_id] -= 1
        if self.common[node_id] == 0:
            self.c[node_id] = -1
        while history:
            node_id, c = history.pop()
            next_id = self.next[node_id][c]
            if self.common[next_id] == 0:
                self.next[node_id][c] = -1
            self.common[node_id] -= 1
            if self.common[node_id] == 0:
                self.c[node_id] = -1
        return True

    def start_with(self, word: str):
        return self.search(word, True)

    def count(self):
        return self.common[0]

    def size(self):
        return len(self.nodes)

    def dfs(self, node_id: int, A: list, words: list):
        if self.accept[node_id]:
            words.append("".join(A))
        for node_id, next_id in self.next[node_id].items():
            if next_id == -1:
                continue
            A.append(chr(self.base + self.c[next_id]))
            self.dfs(next_id, A, words)
            A.pop()

    def get_words(self, node_id):
        words = list()
        self.dfs(node_id, [], words)
        return words

    def get_words_prefix(self, prefix: str):
        if not self.search(prefix, True):
            return []
        words = list()
        A = list(prefix)
        node_id = 0
        for i in range(len(prefix)):
            c = ord(prefix[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return False
            node_id = next_id
        self.dfs(node_id, A, words)
        return words

    def get_maxLCP(self, word: str):
        node_id = 0
        res = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return res
            res += 1
            node_id = next_id
        return res

    def IsContainPrefix(self, word: str):
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return False
            if len(self.accept[next_id]) > 0:
                return True
            node_id = next_id
        return False


Y = SortedMultiset()
Z = SortedMultiset()
TrieTreeX = Trie()
TrieTreeY = Trie()
Q = int(input())
ans = []
for _ in range(Q):
    t, s = input().split()
    if t == "1":
        TrieTreeX.insert(s)
        words = TrieTreeY.get_words_prefix(s)
        for w in words:
            Z.add(w)
            TrieTreeY.erase(w)
    elif t == "2":
        Y.add(s)
        if not TrieTreeX.IsContainPrefix(s):
            Z.add(s)
            TrieTreeY.insert(s)
    ans.append(len(Y) - len(Z))
print(*ans, sep="\n")
