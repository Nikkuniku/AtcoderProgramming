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
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                next_id = len(self.nodes)
                self.nodes.append(next_id)
                self.next.append([-1] * self.charsize)
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
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                pass
                # 今見ている文字列で最後
            self.common[node_id] -= 1
            if self.common[node_id] == 0:
                self.c[node_id] = -1
            node_id = next_id
        self.accept[node_id].pop()
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


TrieTree = Trie()

TrieTree.insert("apple")
# print(TrieTree.search("apple"))
# print(TrieTree.search("app"))
# print(TrieTree.start_with("app"))
TrieTree.insert("app")
print(TrieTree.search("app"))
print(TrieTree.erase("app"))
print(TrieTree.search("app"))
print(TrieTree.count())
print(TrieTree.size())
