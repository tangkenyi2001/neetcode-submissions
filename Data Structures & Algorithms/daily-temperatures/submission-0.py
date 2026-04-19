class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        #stack should be strictly decreasing
        #stack should store (value,index)
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                top=stack.pop()
                res[top[1]]=i-top[1]
            else:
                stack.append([temperatures[i],i])
        return res
