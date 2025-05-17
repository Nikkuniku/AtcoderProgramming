class Trie:
    def __init__(self):
        self.nodes = []
        self.next = []
        self.accept = []
        self.c = []
        self.common = []
        self.Zv = []
        self.fv = []
        self.base = ord("a")
        self.charsize = 26  # 英字分
        # root
        self.nodes.append(0)
        self.next.append([-1] * self.charsize)
        self.accept.append([])
        self.c.append(-1)
        self.common.append(0)
        self.Zv.append(set())
        self.fv.append(False)

    def insert_word(self, word: str, word_id: int, isY: bool):
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                next_id = len(self.nodes)
                self.nodes.append(next_id)
                self.next.append([-1] * self.charsize)
                self.accept.append([])
                self.Zv.append(set())
                self.c.append(c)
                self.common.append(0)
                self.fv.append(False)
            self.next[node_id][c] = next_id
            self.common[node_id] += 1
            if isY:
                self.Zv[next_id].add(word_id)
            node_id = next_id
        self.common[node_id] += 1
        self.accept[node_id].append(word_id)
        if not isY:
            self.fv[node_id] = True

    def search_Y(self, word: str):
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return False
            if self.fv[next_id]:
                return True
            node_id = next_id
        return False

    def search_X(self, word: str):
        node_id = 0
        Zs = set()
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.next[node_id][c]
            if next_id == -1:
                return set()
            node_id = next_id
        for v in self.Zv[node_id]:
            Zs.add(v)
        self.Zv[node_id].clear()
        return Zs


TrieTree = Trie()
Q = int(input())
ans = []
Y = set()
Z = set()
for i in range(Q):
    t, s = input().split()
    t = int(t)
    if t == 1:
        BannedY = TrieTree.search_X(s)
        for j in BannedY:
            Z.add(j)
        TrieTree.insert_word(s, i, False)
    elif t == 2:
        Y.add(i)
        isBanned = TrieTree.search_Y(s)
        if isBanned:
            Z.add(i)
        TrieTree.insert_word(s, i, True)
    ans.append(len(Y) - len(Z))
print(*ans, sep="\n")
