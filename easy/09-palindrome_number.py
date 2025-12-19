class Solution:
    def isPalindrome(self, x: int) -> bool:


        nuermo_invertido =  0
        residuo = x
        
        while residuo > 0:
            # sacar el ultimo numoer
            ultimo = residuo % 10
            residuo = residuo // 10

            nuermo_invertido = nuermo_invertido * 10 + ultimo
        
        if nuermo_invertido != x: 
            return False

        return True

        