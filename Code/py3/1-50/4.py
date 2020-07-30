class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findk(arr1, arr2, k):
            l1, l2 = len(arr1), len(arr2)
            if l1 > l2:
                arr1, arr2 = arr2, arr1
                l1, l2 = l2, l1
            if arr1 == []:
                return arr2[k - 1]
            elif k == 1:
                return min(arr1[0], arr2[0])
            i, j = min(k // 2, l1) - 1, min(k // 2, l2) - 1
            if arr1[i] > arr2[j]: # accept arr2[:j]
                return findk(arr1, arr2[j + 1:], k - j - 1)
            else: # accept arr1[:i]
                return findk(arr1[i + 1:], arr2, k - i - 1)
        l1, l2 = len(nums1), len(nums2)
        l, r = (l1 + l2 + 1) // 2, (l1 + l2 + 2) // 2 # if odd l = r, if even r = l + 1
        return (findk(nums1, nums2, l) + findk(nums1, nums2, r)) / 2