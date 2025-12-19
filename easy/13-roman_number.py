

class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0 
        pre_value = 0

        for letter in s:
            current_value = symbols[letter]

            if pre_value < current_value:
                total += current_value - 2*pre_value
            else:
                total += current_value

            
            pre_value = current_value

        return total

            

Solution().romanToInt("MCMXCIV")
Solution().romanToInt("III")
Solution().romanToInt("LVIII")
Solution().romanToInt("MCMXCIV")





# Logica basica
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         # III
#         # LVIII
#         # MCMXCIV
#         symbols = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         total = 0 
    
#         save_letter = ''
#         for index, letter in enumerate(s):
            
#             if save_letter:
#                 if symbols[save_letter] >= symbols[letter]:
#                     total += symbols[save_letter]
#                     save_letter = letter
#                 else:
#                     total = symbols[letter] - symbols[save_letter] + total
#                     save_letter = ''
#                     continue
#             else:
#                 save_letter = letter


#             if(index == len(s) - 1):
#                 total += symbols[letter]
#         return total


            

# Solution().romanToInt("MCMXCIV")
# Solution().romanToInt("III")
# Solution().romanToInt("LVIII")
# Solution().romanToInt("MCMXCIV")





