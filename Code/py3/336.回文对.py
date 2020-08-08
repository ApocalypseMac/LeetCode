#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#

# @lc code=start
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        revwords = {} # store srverse of each word
        n = len(words)
        for i in range(n):
            wd = words[i][::-1]
            revwords[wd] = i
        #print(revwords)
        res = set()
        
        def isPalindrome(s: str):
            n = len(s)
            if n <= 1:
                return True
            i, j = 0, n - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for i in range(n):
            wd = words[i]
            m = len(wd)
            for j in range(m + 1):
                left, right = wd[:j], wd[j:]
                if isPalindrome(left): # R' + L + R
                    if right in revwords and revwords[right] != i: # if L = ""
                        res.add((revwords[right], i))
                if isPalindrome(right): # L + R + L'
                    if left in revwords and revwords[left] != i: # if R = ""
                        res.add((i, revwords[left]))
        #print(res)
        return list(res)
            
                
# @lc code=end

