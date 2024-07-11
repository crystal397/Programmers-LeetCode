class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 한 번에 인덱스와 리스트의 값을 반복시켜 확인합니다.
        for i, num in enumerate(nums):
            # 찾고자 하는 조합을 위해 target에서 num을 뺀 find_target이 있는지 확인합니다.
            find_target = target - num
            if find_target in nums[i+1:]:
                # 같은 인덱스를 두 번 사용할 수 없지만, 리스트 안에 동일한 값이 있는 경우에는 index를 사용했을 때 i와 같은 인덱스를 찾아내기 때문에 filter를 사용합니다. 
                if num == find_target:
                   return list(filter(lambda x: nums[x] == find_target, range(len(nums))))
                # 그렇지 않을 경우는 index를 사용해서 원하는 조합의 인데스 조합을 반환합니다.
                else:
                   return [i, nums.index(find_target)]
