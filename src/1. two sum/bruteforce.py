from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in nums:
        for j in nums[nums.index(i) + 1 :]:
            if i + j == target:
                first_index = nums.index(i)
                second_index = nums.index(j, first_index + 1)

                return [first_index, second_index]


print(twoSum([3, 3], 6))
