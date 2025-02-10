class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        res=[]
        for i in range(len(nums)):
            while nums[i]//10>0:
                count+=1
                nums[i]=nums[i]//10
            res.append(count)
            count=0
        result = 0
        for i in range(len(res)):
            if (res[i]%2)==1:
                result+=1
        return result
              