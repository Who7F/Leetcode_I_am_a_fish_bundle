class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = -1
        for i, n in enumerate(nums1):
            dst = -1
            for j, m in enumerate(nums2[i:],  start=i):
                print(n,m)
                if n > m:
                    break
                dst += 1
            
            res = max(res, dst)

        return res
