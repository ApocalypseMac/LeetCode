class Solution:
    def minPartitions(self, n: str) -> int:
        return max(ord(ch) - ord('0') for ch in n)