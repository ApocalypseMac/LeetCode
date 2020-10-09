class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def inversegrayCode(n): 
            inv = 0
            while n: 
                inv = inv ^ n
                n = n >> 1
            return inv
        return inversegrayCode(n)
                
            
        

                
            