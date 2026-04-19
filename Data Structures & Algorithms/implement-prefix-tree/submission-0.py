class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEndofWord=False

class PrefixTree:

    def __init__(self):
        self.rootnode=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.rootnode
        for i in word:
            curletter=ord(i)-ord('a')
            if not cur.children[curletter]:
                cur.children[curletter]=TrieNode()
            cur=cur.children[curletter]
        cur.isEndofWord=True

    def search(self, word: str) -> bool:
        cur=self.rootnode
        for i in word:
            curletter=ord(i)-ord('a')
            if not cur.children[curletter]:
                return False
            cur=cur.children[curletter]
        if (cur.isEndofWord==False):
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur=self.rootnode
        for i in prefix:
            curletter=ord(i)-ord('a')
            if not cur.children[curletter]:
                return False
            cur=cur.children[curletter]
        return True
        