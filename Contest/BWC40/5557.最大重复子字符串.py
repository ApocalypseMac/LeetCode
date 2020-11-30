class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        pattern = word
        i = 0
        while len(pattern) <= len(sequence):
            if pattern not in sequence:
                break
            i += 1
            pattern += word
        return i