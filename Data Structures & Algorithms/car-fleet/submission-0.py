class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #just need to catch before they end
        #need to sort the position first, because they can never overtake
        start=[]
        stack=[]
        for i in range(len(position)):
            start.append([position[i],speed[i]])
        start.sort(key=lambda i:i[0], reverse=True) #sort based on position
        for p,s in start:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
            
            
