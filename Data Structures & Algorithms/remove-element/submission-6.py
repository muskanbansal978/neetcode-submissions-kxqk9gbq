class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]  # swap with last
                right -= 1                # shrink window
            else:
                left += 1                 # valid, move forward

        return left  # k = number of valid elements