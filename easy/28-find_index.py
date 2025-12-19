class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n = (len(haystack))
        m =  (len(needle))


        print(n)
        print(m)
        print(n-m+1)
        index = 0

        for i, letter in enumerate(haystack):

            if needle[index] == letter:
                index+=1
            else: 
                index = 0

            if index == len(needle):
                # print(index, len(needle))
                return 0
            
        return -1



haystack = "sadbutsad" 
needle = "sad"

print(Solution().strStr(haystack=haystack, needle=needle))