class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            x = min(give, candies)
            ans[i] += x
            candies -= x
            give += 1
            i = (i + 1) % num_people
        return ans