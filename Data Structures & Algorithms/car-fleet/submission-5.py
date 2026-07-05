class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #basically, can never overtake the at in front
        # so I should compute each car and see if the car after can catch up
        # time taken = (target-postion)/speed
        #first car
        numberofCars=len(position)
        timetakenForCars=[]
        for i in range(numberofCars):
            timetaken=(target-position[i])/speed[i]
            timetakenForCars.append([-1*position[i],timetaken])
        timetakenForCars.sort()
        stack=[timetakenForCars[0][1]]
        for i in range(1,numberofCars):
            if timetakenForCars[i][1]<=stack[-1]:
                continue
            else:
                stack.append(timetakenForCars[i][1])
        return len(stack)
        
