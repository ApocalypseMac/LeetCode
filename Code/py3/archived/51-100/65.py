class Solution:
    def isNumber(self, s: str) -> bool:
        sign_flag = True # sign 
        expsign_flag = True # sign after e
        dec_flag = True # decimal point
        # isdec = False # is decimal part
        exp_flag = True # exponent
        exp_exist = False
        end_flag = True # first space after expression
        val = None
        exponent = None
        n = len(s)
        if n == 0:
            return False
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return False
        #return False
        while i < n:
            if sign_flag and (s[i] == '+' or s[i] == '-'):
                sign_flag = False
                i += 1
            elif exp_exist and expsign_flag and (s[i] == '+' or s[i] == '-'):
                expsign_flag = False
                i += 1
            elif dec_flag and s[i] == '.':
                sign_flag = False
                dec_flag = False
                i += 1
            elif exp_flag and s[i] == 'e' and val:
                sign_flag = False
                dec_flag = False
                exp_flag = False
                exp_exist = True
                i += 1
            elif s[i] == ' ':
                sign_flag = False
                dec_flag = False
                exp_flag = False
                end_flag = False
                expsign_flag = False
                i += 1
            elif end_flag and s[i].isdigit():
                sign_flag = False
                if exp_flag:
                    val = 1
                else:
                    expsign_flag = False
                    exponent = 1
                i += 1
            else:
                return False
        if val:
            if (exp_exist and exponent) or (exp_exist is False and exponent is None):
                return True
        return False