"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""

# date: 2019.9.5

class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        num = []
        if y[0] == "-":
            num.append('-')
            y = y[1:]
        for i in range(1, len(y)+1):
            num.append(y[-i])
        x = ''.join(num)
        x = int(x)
        if x > 2147483647 or x < -2147483648:
            x = 0
        return x