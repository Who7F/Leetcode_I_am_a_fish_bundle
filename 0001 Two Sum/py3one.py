class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDic ={}
        for i, j in enumerate(nums):
            if target - j in myDic:
                return [myDic[target - j], i]
            else:
                myDic[j] = i

        return []