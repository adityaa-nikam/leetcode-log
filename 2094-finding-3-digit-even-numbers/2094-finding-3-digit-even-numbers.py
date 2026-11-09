class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                num = a * 100 + b * 10 + c
                ans.add(num)
        return sorted(ans)