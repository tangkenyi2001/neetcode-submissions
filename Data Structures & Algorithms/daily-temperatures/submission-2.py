class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # naive method is for each of the number, u iterate through the list to see if there is one greater than it. 
        numTemperatures=len(temperatures)
        res=[0 for i in range(numTemperatures)]
        stack=[[temperatures[-1],numTemperatures-1]]
        
        for i in range(numTemperatures-2,-1,-1):
            while stack and temperatures[i]>=stack[-1][0]:
                stack.pop()
            if stack:
                res[i]=stack[-1][1]-i
            stack.append([temperatures[i],i])
        return res
        

            
            