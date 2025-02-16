class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        while n>0:
            nums1.pop()
            n-=1
        nums1+=nums2
        nums1.sort()