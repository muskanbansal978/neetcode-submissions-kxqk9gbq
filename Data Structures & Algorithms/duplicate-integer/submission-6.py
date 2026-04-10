class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_nums=[]
        counter=0
        for i in range(len(nums)):
            if nums[i] not in unique_nums:
                unique_nums.append(nums[i])
            else:
                counter=1
        
        if counter==0:
            return False
        else:
            return True