class Solution:
    # O(n) time O(n) space
    def isValid(self, s: str) -> bool:        
        stack = []
        
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == "{" or s[i] == "(" or s[i] == "[":
                    stack.append(s[i])
                else:
                    if s[i] == "}" and stack[len(stack) - 1] != "{":
                        return False
                    elif s[i] == ")" and stack[len(stack) - 1] != "(":
                        return False
                    elif s[i] == "]" and stack[len(stack) - 1] != "[":
                        return False
                    else:
                        stack.pop()
        
        if len(stack) == 0:
            return True
        else:
            return False
