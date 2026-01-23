class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            tmp = "".join(sorted(s))
            if tmp not in res:
                res[tmp] = []
            
            res[tmp].append(s)
               
        return list(res.values())
