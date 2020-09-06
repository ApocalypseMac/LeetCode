class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        sq1 = dict()
        sq2 = dict()
        for i in nums1:
            temp = i ** 2
            if temp not in sq1:
                sq1[temp] = 1
            else:
                sq1[temp] += 1
        for i in nums2:
            temp = i ** 2
            if temp not in sq2:
                sq2[temp] = 1
            else:
                sq2[temp] += 1
        res = 0
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            for j in range(i + 1, n1):
                prod = nums1[i] * nums1[j]
                if prod in sq2:
                    res += sq2[prod]
        for i in range(n2):
            for j in range(i + 1, n2):
                prod = nums2[i] * nums2[j]
                if prod in sq1:
                    res += sq1[prod]
        return res