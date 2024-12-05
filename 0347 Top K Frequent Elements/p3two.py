class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        buckets = [0] * len(nums)
        

        for key, val in counter.items():
            print(val, key)
            if buckets[val -1] == 0:
                buckets[val -1] = [key]
            else:
                buckets[val - 1].append(key)

        anc = []
        for i in range(len(nums) -1, -1, -1):
            if buckets[i] != 0:
                anc.extend(buckets[i])
            if len(anc) == k:
                return anc
        return [0]
