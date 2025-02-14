class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        count=0
        for i in reversed(range(len(arr)-1)):
            if arr[i]==0:
                count+=1
                arr.insert(i,0)
        while count>0:
            arr.pop()
            count-=1
        