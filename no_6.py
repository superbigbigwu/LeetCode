"""
Z字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 :

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""

# date: 2019.9.5

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        elif numRows == 1:
            return s
        else:
            length = len(s)
            nums = []
            no = []
            a = 0
            flag = True
            for i in range(length):
                no.append(a)
                if flag:
                    a += 1
                else:
                    a -= 1
                if a == 0:
                    flag = True
                if a == numRows-1:
                    flag = False
            for i in range(numRows):
                while i in no:
                    b = no.index(i)
                    nums.append(s[b])
                    no[b] = '#'
            Zz = ''.join(nums)
            return Zz


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         length = len(s)
#         m = 2 * numRows - 2
#         n = numRows - 2
#         if not s:
#             return ''
#         elif numRows == 1:
#             return s
#         elif len(s) <= numRows:
#             return s
#         elif length <= m:
#             nums = []
#             b = length
#             if length <= numRows:
#                 return s
#             else:
#                 for i in range(numRows):
#                     if i == 0 or i == numRows-1:
#                         nums.append(s[i])
#                     else:
#                         nums.append(s[i])
#                         if b+i > m:
#                             nums.append(s[length-i])
#             Zz = ''.join(s)
#             return Zz
#         else:
#             a = length // m
#             b = length % m
#             x = b
#             nums = []
#             nn = n
#             for i in range(numRows):
#                 if i == 0 or i == numRows-1:
#                     for p in range(a):
#                         nums.append(s[i + p*m])
#                     if x > 0:
#                         nums.append(s[i + a*m])
#                         x -= 1
#                 else:
#                     for p in range(a):
#                         nums.append(s[i + p*m])
#                         nums.append(s[numRows-1 + p*m + nn])
#                     nn -= 1    
#                     if x > 0:
#                         nums.append(s[i + a*m])
#                         x -= 1
#                     if b+i > m:
#                         nums.append(s[a*m-1+m-i])
#             Zz = ''.join(nums)
#             return Zz