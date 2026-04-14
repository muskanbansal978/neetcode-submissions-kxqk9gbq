class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        counter=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count=0
                counter.append(count)
            else:
                count+=1
                counter.append(count)
        return max(counter)
