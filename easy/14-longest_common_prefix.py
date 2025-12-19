from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        prefix = strs[0] if strs else ""

        if prefix == "" : 
            return ""

        if len(strs) == 1: 
            return strs[0]

        index  = 0

        while index < len(prefix):
            
            for word in strs[1:]:
                
                if index > len(word) -1 or  word[index] != prefix[index]:
                    return prefix[:index]
                
            index += 1

        return prefix[:index]
        # return prefix[:next((i for i in range(len(prefix)) if any(s[i:i+1] != prefix[i:i+1] for s in strs[1:])), len(prefix))]
    

res1 = Solution().longestCommonPrefix(["flower","flower","flower","flower","flower"])
res2 = Solution().longestCommonPrefix(
["flower","flow","flight"]
)

print(res1)
print(res2)