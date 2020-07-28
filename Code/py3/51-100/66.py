class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp, carry = 0, 1
        for i in range(len(digits)):
            temp = digits[-(i+1)] + carry
            carry = temp // 10
            digits[-(i+1)] = temp % 10
            if not carry:
                return digits
        if carry:
            digits.insert(0, carry)
        return digits