class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        anc = []
        l = len(nums)
        i = 0
        if nums[l - 1] < 0:
            return anc
      
        while nums[i] < 0:
            
            lo = i + 1
            hi = l - 1

            while lo < hi:

                if nums[lo] + nums[hi] == -nums[i]:
                    anc.append([nums[i], nums[lo], nums[hi]])

                    while nums[hi] == nums[hi - 1]:
                        hi -= 1

                    while lo > l and nums[lo] == nums[lo + 1]:
                        lo += 1

                    lo += 1
                    hi -= 1
              
                elif nums[lo] + nums[hi] < -nums[i]: 
                    lo += 1

                elif nums[lo] + nums[hi] > -nums[i]:
                    hi -= 1


            i += 1
            while nums[i] == nums[i - 1]:
                i += 1

        if i + 2 < l and nums[i] + nums[i + 2] == 0:
            anc.append([0,0,0])

        return anc