class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for querie in queries:
       
            start = querie[0]
            end = querie[1] + 1
            step = querie[2]
            val = querie[3]

            if step == 0:
                continue

            for idx in range(start, end, step):
                nums[idx] = (nums[idx] * val) % 1000000007


        result = 0
        for n in nums:
            result ^= n
        
        return result