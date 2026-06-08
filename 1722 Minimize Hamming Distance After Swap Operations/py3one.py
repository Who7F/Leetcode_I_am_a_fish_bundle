class UnionFind:
    def __init__(self):
        self.parent = {}
    
    def union(self, el1, el2):
        self.parent[self.find(el2)] = self.find(el1)

    def find(self, el):
        p = self.parent.get(el, el)
        if p!=el: p = self.parent[el] = self.find(p)
        return p

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)

        per = UnionFind()

        for a, b in allowedSwaps:
            per.union(a, b)

        groups = defaultdict(list)


        for i in range(n):
            groups[per.find(i)].append(i)


        res = 0

        for idx in groups.values():
            freq = {}

            for i in idx:
                freq[source[i]] = freq.get(source[i], 0) + 1

            for i in idx:
                if freq.get(target[i], 0) > 0:
                    freq[target[i]] -= 1
                else:
                    res += 1

        return res
        
