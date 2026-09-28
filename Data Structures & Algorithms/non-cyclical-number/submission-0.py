class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n:int):
            strN=str(n)
            number=0
            for i in strN:
                number+=pow(int(i),2)
            return number
        
        hashset={}
        curN=n
        while True:
            curN=square(curN)
            if curN==1:
                return True
            elif curN in hashset:
                return False
            else:
                hashset[curN]=1
        
        