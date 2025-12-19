from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Recorremos desde el final hacia el inicio
        for i in range(len(digits)-1, -1, -1):
            
            # Si el dígito es menor que 9, solo sumamos 1 y regresamos
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # Si es 9, lo convertimos en 0 y seguimos el carry
            digits[i] = 0
        
        # Si todos eran 9, llegamos aquí -> ejemplo: 999 -> 1000
        return [1] + digits


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

#         amount = 0 
#         for i,di in enumerate(digits):
#             amount += di*pow(10,len(digits)-(i+1))

#         amount +=1

#         arr = list(str(amount))
#         arr = [int(x) for x in arr]
#         print(arr)
#         return arr
    


    

re =Solution().plusOne([9,5,9])
print(re)

