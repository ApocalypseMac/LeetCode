#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        word += '#'
        T = self.root
        for ch in word:
            if ch not in T:
                T[ch] = {}
            T = T[ch]


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        word += '#'
        n = len(word)
        def helper(curr, k):
            if word[k] != '.':
                if word[k] not in curr:
                    return False
                if k == n - 1:
                    return True
                curr = curr[word[k]]
                if helper(curr, k + 1):
                    return True
            else:
                for v in curr.values():
                    if helper(v, k + 1):
                        return True
            return False
        
        return helper(self.root, 0)






# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

