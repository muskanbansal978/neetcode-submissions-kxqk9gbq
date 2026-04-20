class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paranthesis={")":"(","]":"[","}":"{"}

        for i in s:
            if i in paranthesis:
                if stack and paranthesis[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False


                

        