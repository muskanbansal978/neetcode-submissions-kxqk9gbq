class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for word in strs:
            count=[0]*26
            for char in word:
                 count[ord(char)-ord('a')]+=1
            tuple_count=tuple(count)
            if tuple_count not in result:
                result[tuple_count]=[]
            result[tuple_count].append(word)
        
        return list(result.values())