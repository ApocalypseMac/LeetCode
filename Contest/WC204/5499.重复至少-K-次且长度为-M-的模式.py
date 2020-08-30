class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        if m * k > n:
            return False
        
        count = 0
        #maxcount = 0
        for i in range(n - m * k + 1):
            mode = arr[i:i+m]
            lo, hi = i + m, i + 2 * m
            count = 1
            while hi <= n:
                if arr[lo:hi] == mode:
                    count += 1
                    lo += m
                    hi += m
                else:
                    break
                if count >= k:
                    return True
                    
        return False
            
            