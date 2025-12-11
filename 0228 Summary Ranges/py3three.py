class Solution:
    def chunkBy(self, nums):
        temp = [nums[0]]
        anc = []

        for i in range(len(nums) - 1):
            
            if nums[i] + 1 != nums[i + 1]:
                anc.append(temp)
                temp = []
            temp.append(nums[i + 1])

        anc.append(temp)  
        
        return anc

    def getHeadTail(self, chunk):
        head = chunk[0]
        tail = chunk[-1]
        return(head, tail)

    def getAnc(self, headTail):
        if headTail[0] == headTail[1]:
            return str(headTail[0])
        return str(headTail[0]) + "->" + str(headTail[1])


    def summaryRanges(self, nums: List[int]) -> List[str]:
        anc = []

        chunk = self.chunkBy(nums)
        headTail = list(map(self.getHeadTail, chunk))
        anc = list(map(self.getAnc, headTail))
        
        return anc
