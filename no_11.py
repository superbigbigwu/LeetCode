"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""

# date: 2019.9.8

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        i, j, S = 0, length-1, 0
        while i < j:
            S = max(S, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return S