class TrieTree:
    def __init__(self):
        self.nodes = []
        self.next = []
        self.accept = []
        self.c = []
        self.common = []
        self.base = ord("a")
        self.charsize = 26  # 英字分
        # root
        self.nodes.append(0)
        self.next.append([-1] * self.charsize)
        self.accept.append([])
        self.c.append(-1)
        self.common.append(0)
        self.res = 0

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
            self.res += self.common[node_id]
        return True if prefix else len(self.accept[node_id]) > 0

    def start_with(self, word: str):
        return self.search(word, True)

    def count(self):
        return self.common[0]

    def size(self):
        return len(self.nodes)


N = int(input())
S = list(input().split())
Trie = TrieTree()
for s in S:
    Trie.search(s)
    Trie.insert(s)
ans = Trie.res
print(ans)
