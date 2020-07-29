class Solution:
    def intToRoman(self, num: int) -> str:
        r0 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        r1 = ['', 'X', 'XX' ,'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        r2 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        r3 = ['', 'M', 'MM', 'MMM']
        m0, m1, m2, m3 = num % 10, (num % 100) // 10, (num % 1000) // 100, num // 1000
        return r3[m3] + r2[m2] + r1[m1] + r0[m0]