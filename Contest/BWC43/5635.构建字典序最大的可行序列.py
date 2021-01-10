class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        l = 2 * n - 1
        res = [0] * l

        def maxlex(a, b):
            for x, y in zip(a, b):
                if x > y:
                    return a[:]
                elif x < y:
                    return b[:]
            return a[:]
        
        flag = False
        def helper(state, arr, idx):
            nonlocal res, flag
            if flag:
                return
            if state == 0:
                flag = True
                res = maxlex(res, arr)
                return
            for i in range(n, 0, -1):
                if (state >> (i - 1)) & 1:
                    if arr[idx] == 0 :
                        if i == 1 or (idx + i < l and arr[idx+i] == 0):
                            state ^= 1 << (i - 1) 
                            idx1 = idx + 1
                            arr[idx] = i
                            if i > 1:
                                arr[idx+i] = i
                            while idx1 < l:
                                if arr[idx1] == 0:
                                    break
                                idx1 += 1
                            helper(state, arr, idx1)
                            state ^= 1 << (i - 1) 
                            arr[idx] = 0
                            if i > 1:
                                arr[idx+i] = 0
        
        helper(2 ** n - 1, [0] * l, 0)
        

        return res
        
        