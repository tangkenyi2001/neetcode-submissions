class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #loop through all the strings
        # create a hashmap that maps the sorted words to a list that includes the new words
        # hashset={"act":["act","cat"]}
        hashset=defaultdict(list)
        for word in strs:
            key="".join(sorted(word))
            hashset[key].append(word)
        res=[]
        for lists in hashset:
            res.append(hashset[lists])

        return res