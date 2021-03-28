class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        return (primeFactors - 3 * max(0, (primeFactors - 2) // 3)) * pow(3, int(max(0, (primeFactors - 2) // 3)), 10 ** 9 + 7) % (10 ** 9 + 7)