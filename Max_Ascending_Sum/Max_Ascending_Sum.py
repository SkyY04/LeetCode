class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        count=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                count=count+nums[i]
                result = max(result, count)
            else:
                count=nums[i]
                result = max(result, count)
        return result