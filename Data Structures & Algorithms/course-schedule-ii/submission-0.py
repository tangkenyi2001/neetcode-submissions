from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #indegree stands for number of prereqs
        indegree=[0]*numCourses
        prereqtoCourse=defaultdict(set)
        for course,prereq in prerequisites:
            indegree[course]+=1
            prereqtoCourse[prereq].add(course)
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            curCourse=q.popleft()
            res.append(curCourse)
            for course in prereqtoCourse[curCourse]:
                indegree[course]-=1
                if indegree[course]==0:
                    q.append(course)
        
        if len(res)==numCourses:
            return res
        else:
            return []