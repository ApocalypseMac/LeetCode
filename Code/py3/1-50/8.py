class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        result = 0
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        negflag = False
        if i >= len(str):
            return 0
        elif str[i] == '-':
            negflag = True
            i += 1
        elif str[i] == '+':
            i += 1
        intmin = -2147483648
        intmax = 2147483647
        while i < len(str) and str[i].isdigit():
            '''
            if negflag:
                if result > 214748364:
                    return intmin
                elif result == 214748364 and str[i] > '8':
                    return intmin
                else:
                    result = result * 10 + (ord(str[i]) - 48)
            else:
                if result > 214748364:
                    return intmax
                elif result == 214748364 and str[i] > '7':
                    return intmax
                else:
                    result = result * 10 + (ord(str[i]) - 48)
            '''
            result = result * 10 + (ord(str[i]) - 48)
            if negflag:
                if result > -intmin:
                    return intmin
            else:
                if result > intmax:
                    return intmax
            i += 1
        if negflag:
            return -result
        else:
            return result