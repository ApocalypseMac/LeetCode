class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
#         s1 = sum(nums1)
#         s2 = sum(nums2)
#         diff = s1 - s2
#         if diff < 0:
#             nums1, nums2 = nums2, nums1
#             diff = -diff
            
#         l1, l2 = len(nums1), len(nums2)
#         if l1 > l2 * 6:
#             return -1
#         nums1.sort()
#         nums2.sort()
#         res = 0
#         i = l1 - 1
#         j = 0
#         while diff > 0 and (i >= 0 or j < l2):
#             if i >= 0 and j < l2:
#                 if nums1[i] - 1 > 6 - nums2[j]:
#                     diff -= nums1[i] - 1
#                     res += 1
#                     i -= 1
#                 else:
#                     diff -= 6 - nums2[j]
#                     res += 1
#                     j += 1
#             elif i >= 0:
#                 diff -= nums1[i] - 1
#                 res += 1
#                 i -= 1
#             else:
#                 diff -= 6 - nums2[j]
#                 res += 1
#                 j += 1
                
#         return res
            
        l1, l2 = len(nums1), len(nums2)
        if l1 < l2:
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1
        if l1 > l2 * 6:
            return -1
        s1, s2 = 0, 0
        c1 = [0] * 7
        c2 = [0] * 7
        for num in nums1:
            s1 += num
            c1[num] += 1
        for num in nums2:
            s2 += num
            c2[num] += 1
        res = 0
        def minval(c):
            for i in range(1, 7):
                if c[i]:
                    return i
        
        
        def maxval(c):
            for i in range(6, 0, -1):
                if c[i]:
                    return i
        while s1 != s2:
            diff = s1 - s2
            res += 1
            if diff > 0:
                mx1 = maxval(c1)
                mn2 = minval(c2)
                flag = -1
                change1 = mx1 - 1
                change2 = 6 - mn2 
                if change1 >= change2:
                    flag = 1
                else:
                    flag = 2
                if diff > max(change1, change2):
                    if flag == 1:
                        s1 -= change1
                        c1[mx1] -= 1
                        c1[1] += 1
                    else:
                        s2 += change2
                        c2[mn2] -= 1
                        c2[6] += 1
                else:
                    return res
            else:
                mn1 = minval(c1)
                mx2 = maxval(c2)
                flag = -1
                change1 = 6 - mn1
                change2 = mx2 - 1
                if change1 >= change2:
                    flag = 1
                else:
                    flag = 2
                if -diff > max(change1, change2):
                    if flag == 1:
                        s1 += change1
                        c1[mn1] -= 1
                        c1[6] += 1
                    else:
                        s2 -= change2
                        c2[mx2] -= 1
                        c2[1] += 1
                else:
                    return res
        return res
