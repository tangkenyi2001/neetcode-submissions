from collections import defaultdict,deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #topological sort, so the idea is to have a queue, that stores the next course
        queue=deque([])
        # Initialize a dictionary where every new key automatically defaults to a set
        courseToPrereq = defaultdict(set)
        prereqToCourse = defaultdict(set)
        for course, prereq in prerequisites:
            courseToPrereq[course].add(prereq)
            prereqToCourse[prereq].add(course)

        #
        for prereq in range(numCourses):
            if prereq not in courseToPrereq:
                queue.append(prereq)
        count=0
        while queue:
            curCourse=queue.popleft()
            count+=1
            #iterate through current 
            for i in prereqToCourse[curCourse]:
                if len(courseToPrereq[i])==0:
                    # if its already empty
                    continue
                courseToPrereq[i].remove(curCourse)
                if len(courseToPrereq[i])==0:
                    queue.append(i)
        #count is number of courses with no prereq
        return count==numCourses
# s=Solution()
# print(s.canFinish(numCourses = 2, prerequisites = [[0,1]]))