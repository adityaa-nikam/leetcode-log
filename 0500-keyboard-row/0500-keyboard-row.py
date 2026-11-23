class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {}

        for ch in "qwertyuiop":
            rows[ch] = 1

        for ch in "asdfghjkl":
            rows[ch] = 2
        for ch in "zxcvbnm":
            rows[ch] = 3
        result = []
        for word in words:
            first_row = rows[word[0].lower()]

            if all(rows[ch.lower()] == first_row for ch in word):
                result.append(word)

        return result