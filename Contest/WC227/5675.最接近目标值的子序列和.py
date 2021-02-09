class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        if n % 2 == 1:
            nums.append(0)
            n += 1
        n1 = n // 2
        nums1, nums2 = nums[:n1], nums[n1:]
        # print(nums1, nums2)
        sum1 = [-goal] * (1 << n1)
        sum2 = [0] * (1 << n1)
        for mask in range(1, 1 << n1):
            for k in range(n1):
                if (mask >> k) & 1:
                    sum1[mask] = sum1[mask ^ (1 << k)] + nums1[k]
                    sum2[mask] = sum2[mask ^ (1 << k)] + nums2[k]
                    break
        sum1 = sorted(sum1)
        sum2 = sorted(sum2)
        res = 10 ** 9
        # print(sum1)
        # print(sum2)
        i2 = (1 << n1) - 1
        i1 = 0
        while i1 < (1 << n1) and i2 >= 0:
            tmp = sum1[i1] + sum2[i2]
            if tmp == 0:
                return 0
            # print(i1, i2, tmp)
            res = min(res, abs(tmp))
            if tmp > 0:
                i2 -= 1
            else:
                i1 += 1
        return res
            