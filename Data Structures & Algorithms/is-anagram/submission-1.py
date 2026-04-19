class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmapS=defaultdict(int)
        hashmapT=defaultdict(int)

        for char in s:
            hashmapS[char]=hashmapS.get(char,0)+1
        for char in t:
            hashmapT[char]=hashmapT.get(char,0)+1
            
        for key,value in hashmapT.items():
            if hashmapS.get(key,0)<value:
                return False
        return True

