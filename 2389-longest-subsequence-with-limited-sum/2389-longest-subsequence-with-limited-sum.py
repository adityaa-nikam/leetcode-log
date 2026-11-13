class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        answer = []
        for q in queries:
            count = bisect_right(prefix, q)
            answer.append(count)
        return answer