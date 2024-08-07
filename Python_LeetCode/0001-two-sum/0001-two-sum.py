class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in dict:
                return [dict[remain], idx]
            else:
                dict[num] = idx