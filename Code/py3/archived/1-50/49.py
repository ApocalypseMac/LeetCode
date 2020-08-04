class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        for s in strs:
            freq = [0] * 26
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            if tuple(freq) in dic:
                dic[tuple(freq)].append(s)
            else:
                dic[tuple(freq)] = [s]
        for v in dic.values():
            result.append(v)
        return result