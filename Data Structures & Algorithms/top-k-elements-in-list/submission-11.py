class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frequency=[[] for i in range(len(nums)+1)]

        for i in nums:
            count[i]=count.get(i,0)+1
        
        for num,feq in count.items():
                frequency[feq].append(num)

        result=[]
        for i in range(len(frequency)-1,0,-1):
            for res in frequency[i]:
                result.append(res)
            if len(result)==k:
                return result

        
