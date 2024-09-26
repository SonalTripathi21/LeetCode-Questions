class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = [None] * 26

class Solution:
    def sumPrefixScores(self, words):
        root = TrieNode()

        for w in words:
            node = root
            for ch in w:
                index = ord(ch) - ord('a')
                if not node.children[index]:
                    node.children[index] = TrieNode()
                node = node.children[index]
                node.count += 1

        ans = []
        for w in words:
            sum = 0
            node = root
            for ch in w:
                index = ord(ch) - ord('a')
                node = node.children[index]
                sum += node.count
            ans.append(sum)
        return ans    