class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            find_target = target - num
            if find_target in nums[i+1:]:
                if num == find_target:
                   return list(filter(lambda x: nums[x] == find_target, range(len(nums))))
                else:
                   return [i, nums.index(find_target)]