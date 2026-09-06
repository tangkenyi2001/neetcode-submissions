class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car cannot be faster than the car in front of it.
        # basically want to see if each car can reach faster than the car in front
        # time taken for car to reach.
        timetaken=list(zip(position,speed))
        timetaken.sort(reverse=True)
        # print(timetaken)
        timetaken=[((target-timetaken[i][0])/timetaken[i][1]) for i in range(len(timetaken))]
        #basically should be descending
        res=[timetaken[0]]

        for i in range(1,len(timetaken)):
            if timetaken[i]>res[-1]:
                res.append(timetaken[i])
        return len(res)
        