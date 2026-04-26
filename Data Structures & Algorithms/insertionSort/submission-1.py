class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            j = i - 1
            curr = pairs[i]
            while j >= 0 and pairs[j].key > curr.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = curr
            res.append(deepcopy(pairs))
        
        return res