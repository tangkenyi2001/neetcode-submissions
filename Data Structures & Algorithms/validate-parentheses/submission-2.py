class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ob=['(','{','[']
        cb=[')','}',']']
        for i in s:
            if i in ob:
                stack.append(i)
            else:
                if stack and i==')' and stack[-1]=='(':
                    stack.pop()
                elif stack and i=='}' and stack[-1]=='{':
                    stack.pop()
                elif stack and i==']' and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False