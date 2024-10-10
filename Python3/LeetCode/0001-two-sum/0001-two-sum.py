class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            n = target - num
            if n in dic.keys():
                return [dic[n], idx]
            else:
                dic[num] = idx
            
