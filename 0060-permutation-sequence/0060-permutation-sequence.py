class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        result = []

        k -= 1

        for i in range(n, 0, -1):
            block_size = self.factorial(i - 1)

            index = k // block_size
            result.append(numbers[index])
            numbers.pop(index)

            k %= block_size

        return "".join(result)

    def factorial(self, x: int) -> int:
        result = 1

        for i in range(2, x + 1):
            result *= i

        return result