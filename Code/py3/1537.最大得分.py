#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] 最大得分
#

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        #cross1 = dict() # index when element equal, cross1[index1] = index2
        #cross2 = dict() # cross1[index2] = index1
        n1, n2 = len(nums1), len(nums2)
        partsum1 = [] # calculate [intersect1, intersect2)
        partsum2 = []
        i, j = 0, 0
        temp1, temp2 = 0, 0
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                temp2 += nums2[j]
                j += 1
            elif nums1[i] < nums2[j]:
                temp1 += nums1[i]
                i += 1
            else:
                partsum1.append(temp1)
                partsum2.append(temp2)
                temp1 = nums1[i]
                temp2 = nums2[j]
                i += 1
                j += 1
        while i < n1:
            temp1 += nums1[i]
            i += 1
        while j < n2:
            temp2 += nums2[j]
            j += 1
        partsum1.append(temp1)
        partsum2.append(temp2)
        n = len(partsum1)
        res = 0
        for i in range(n):
            res += max(partsum1[i], partsum2[i])
            res %= 10 ** 9 + 7
        return res
# @lc code=end

