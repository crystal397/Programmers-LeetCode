class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for idx, ele in enumerate(nums):
            mate = target - ele
            if mate in hash_table:
                return [idx, hash_table[mate]]
            hash_table[ele] = idx