class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        start=[(p,s) for p,s in zip(position,speed)]
        start.sort(key=lambda x:x[0],reverse=True)
        stack=[]
        for i in start:
            stack.append((target-i[0])/i[1])   #how long it takes to reach the finish line
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
            
