class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for c1 in word1:
            idx = ord(c1) - ord('a')
            freq1[idx] += 1
        for c2 in word2:
            idx = ord(c2) - ord('a')
            freq2[idx] += 1
        f1, f2 = [], []
        for i in range(26):
            if freq1[i] == 0 and freq2[i] == 0:
                continue
            elif freq1[i] == 0 or freq2[i] == 0:
                return False
            else:
                f1.append(freq1[i])
                f2.append(freq2[i])
        return sorted(f1) == sorted(f2)