class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        anc = []
        frt = nums[0]
        lst = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == lst +1:
                lst = nums[i]   
            else:  
                if frt == lst:
                    anc.append(str(frt))
                else:
                    anc.append(f"{frt}->{lst}")
                frt = nums[i]
                lst = nums[i]

            i += 1
        if frt == lst:
            anc.append(str(frt))
        else:
            anc.append(f"{frt}->{lst}")    


        return anc