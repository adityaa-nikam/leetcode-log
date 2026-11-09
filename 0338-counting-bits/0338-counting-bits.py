class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            num = i
            while num > 0:
                count += num % 2
                num = num // 2
            ans.append(count)
        return ans