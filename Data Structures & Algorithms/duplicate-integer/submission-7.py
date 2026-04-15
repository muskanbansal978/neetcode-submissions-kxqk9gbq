class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=[]
        for i in range(len(nums)):
            if nums[i] not in count:
                count.append(nums[i])
            else:
                return True
        return False