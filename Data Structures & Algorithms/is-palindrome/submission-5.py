class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric =''.join(char.lower() for char in s if char.isalnum())
        left=0
        right=len(alphanumeric)-1

        while left < right:
            if alphanumeric[left] != alphanumeric[right]:
                return False
            
            else:
                left+=1
                right-=1

        return True
        