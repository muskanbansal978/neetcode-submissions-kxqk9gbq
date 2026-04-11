class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            desired_value = target - nums[i]
            if desired_value in nums[i+1:]:
                return [i, nums.index(desired_value, i+1)]