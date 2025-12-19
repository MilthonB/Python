class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # array_words = s.strip().split(" ")
        # return len(array_words[-1])

        return len(s.split()[-1])


re = Solution().lengthOfLastWord("   fly me   to   the moon  ")


print(re)



