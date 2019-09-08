"""
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
"""

# date: 2019.9.8

class Solution:
    def romanToInt(self, s: str) -> int:
        number1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        number2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        length = len(s)
        num = 0
        i = 0
        while i < length:
            if s[i] in ['V', 'L', 'D', 'M']:
                num += number1[s[i]]
                i += 1
            else:
                if i+1 < length:
                    if s[i:i+2] in number2:
                        num += number2[s[i:i+2]]
                        i += 2
                    else:
                        num += number1[s[i]]
                        i += 1
                else:
                    num += number1[s[i]]
                    i += 1
        return num