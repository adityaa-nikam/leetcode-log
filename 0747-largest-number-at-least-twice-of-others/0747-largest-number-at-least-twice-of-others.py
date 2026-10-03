class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)
        second_largest = max(num for num in nums if num != largest)

        if largest >= 2 * second_largest:
            return index
        return -1