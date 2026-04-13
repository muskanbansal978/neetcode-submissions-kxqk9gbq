class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        
        bucket =[[] for _ in range(len(nums)+1)]
        for num,freq in count.items():
            bucket[freq].append(num)
        
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result
       
        