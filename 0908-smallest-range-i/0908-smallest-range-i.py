class Solution:
    def smallestRangeI(self, nums, k):
        minimum = min(nums)
        maximum = max(nums)
        return max(0, (maximum - k) - (minimum + k))