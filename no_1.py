class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size-1):
            for j in range(i+1,size):
                sum = nums[i] + nums[j]
                if target == sum:
                    return(i, j)