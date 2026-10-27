
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(start, end):
            if end - start < 2:
                return (start, start)
            chars = set(s[start:end])
            for i in range(start, end):
                ch = s[i]
                if ch.swapcase() not in chars:
                    left = solve(start, i)
                    right = solve(i + 1, end)
                    left_len = left[1] - left[0]
                    right_len = right[1] - right[0]
                    if left_len >= right_len:
                        return left
                    else:
                        return right
            return (start, end)

        start, end = solve(0, len(s))
        return s[start:end]
