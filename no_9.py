"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

# date: 2019.9.7


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
        
        # if x < 0:
        #     return False
        # y = str(x)
        # length = len(y)
        # if length == 1:
        #     return True
        # elif y[-1] == '0':
        #     return False
        # else:
        #     for i in range(length//2):
        #         if y[i] == y[-i-1]:
        #             flag = True
        #         else:
        #             flag = False
        #             break
        #     if flag:
        #         return "true"
        #     else:
        #         return "false" 