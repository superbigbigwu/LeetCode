"""
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
"""

# date: 2019.9.8

class Solution:
    def intToRoman(self, num: int) -> str:
        number = ''
        if num > 1000:
            a = num // 1000
            number += a * 'M'
            num = num % 1000
        if num == 1000:
            number += 'M'
            num = 0
        if num > 900:
            number += "CM"
            num = num % 900
        if num == 900:
            number += 'CM'
            num = 0
        if num > 500:
            number += 'D'
            num = num % 500
        if num == 500:
            number += 'D'
            num = 0
        if num > 400:
            number += 'CD'
            num = num % 400
        if num == 400:
            number += 'CD'
            num = 0
        if num > 100:
            b = num // 100
            number += b * 'C'
            num = num % 100
        if num == 100:
            number += 'C'
            num = 0
        if num > 90:
            number += 'XC'
            num = num % 90
        if num == 90:
            number += 'XC'
            num = 0
        if num > 50:
            number += 'L'
            num = num % 50
        if num == 50:
            number += 'L'
            num = 0
        if num > 40:
            number += 'XL'
            num = num % 40
        if num == 40:
            number += 'XL'
            num = 0
        if num > 10:
            c = num // 10
            number += c * 'X'
            num = num % 10
        if num == 10:
            number += 'X'
            num = 0
        if num == 9:
            number += 'IX'
            num = 0
        if num > 5:
            number += 'V'
            num = num % 5
        if num == 5:
            number += 'V'
            num = 0
        if num == 4:
            number += 'IV'
            num = 0
        if num > 0:
            number += num * 'I'
        return number