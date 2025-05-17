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


TrieTree = Trie()

TrieTree.insert("apple")
# print(TrieTree.search("apple"))
# print(TrieTree.search("app"))
# print(TrieTree.start_with("app"))
TrieTree.insert("app")
TrieTree.insert("apples")
TrieTree.insert("aaples")
print(TrieTree.search("app"))
# print(TrieTree.erase("app"))
print(TrieTree.search("app"))
print(TrieTree.count())
print(TrieTree.size())
print(TrieTree.get_words_prefix("ap"))
print(TrieTree.IsContainPrefix("applesa"))
