class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, enum in enumerate(nums):
            if enum==target:
                return i
        return -1
        
        