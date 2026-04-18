class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #arr[-1]=[-1]
        for i in range(0,len(arr)-1):
            arr[i]=max(arr[i+1:len(arr)])
        arr[-1]=-1
        
        return arr

            