class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        charset = set(allowed)
        res = 0
        for wd in words:
            for ch in wd:
                if ch not in charset:
                    break
            else:
                res += 1
        return res