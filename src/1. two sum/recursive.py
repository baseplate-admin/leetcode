from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    def recursive(_lst: List[int]):
        lst = list(_lst)
        first_item = lst.pop(0)
        for i in lst:
            if first_item + i == target:
                first_index = nums.index(first_item)
                last_index = nums.index(i, first_index + 1)
                return [first_index, last_index]

        return recursive(lst)

    return recursive(nums)


print(twoSum([3, 3], 6))
