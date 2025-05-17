class Trie:
    class Node:
        def __init__(self, c_=-1):
            self.child = [-1] * 26
            self.accept = []
            self.c = c_
            self.common = 0

    def __init__(self):
        self.nodes = [self.Node()]
        self.base = ord("a")
        self.res = 0

    def add(self, word: str, word_id: int) -> None:
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.nodes[node_id].child[c]
            if next_id == -1:
                next_id = len(self.nodes)
                self.nodes.append(self.Node(c))
                self.nodes[node_id].child[c] = next_id
            self.nodes[node_id].common += 1
            node_id = next_id
        self.nodes[node_id].common += 1
        self.nodes[node_id].accept.append(word_id)

    def insert(self, word: str) -> None:
        self.add(word, self.nodes[0].common)

    def search(self, word: str, prefix: bool = False) -> bool:
        node_id = 0
        for i in range(len(word)):
            c = ord(word[i]) - self.base
            next_id = self.nodes[node_id].child[c]
            if next_id == -1:
                return False
            node_id = next_id
            self.res += self.nodes[node_id].common
        return True if prefix else len(self.nodes[node_id].accept) > 0

    def start_with(self, prefix: str) -> bool:
        return self.search(prefix, True)

    def count(self) -> int:
        return self.nodes[0].common

    def size(self) -> int:
        return len(self.nodes)

    def searchword_kth(self, k: int):
        if self.count() < k:
            return None
        node_id = 0
        res = []
        temp = 0
        while 1:

            for c in range(self.charsize):
                next_id = self.nodes[c]
                if (temp + self.nodes[next_id].common) >= k:
                    break
                temp += self.nodes[next_id].common
            node_id = next_id


N = int(input())
S = list(input().split())
trietree = Trie()
for s in S:
    trietree.search(s)
    trietree.insert(s)
ans = trietree.res
print(ans)
