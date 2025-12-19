# class Solution:
#     def addBinary(self, a: str, b: str) -> str:

#         rules ={
#             '00':'0',
#             '01':'1',
#             '10':'1',
#             '11':'10'
#         }
#         carry = 0

#         res = 0 

#         if len(a) < len(b):
#             s = len(b) - len(a)
#             a = '0'*s+a
#             res = len(a)-1
#         else:
#             s = len(a) - len(b)
#             b = '0'*s+b
#             res = len(b)-1

#         # print(b)

#         stack = ''

#         for i in range(res, -1,-1):

#             if carry:
#                 res1 = rules[f'{carry}{a[i]}']
#                 res2 = rules[f'{res1}{b[i]}']
#                 if res2 == '10':
#                     carry = '1'
#                     stack+='0'
#                     continue
#                 else:
#                     stack += res2
#                     continue
            

#             bin =  f'{a[i]}{b[i]}'
#             res3 = rules[bin]

#             if res3 == '10':
#                 carry = '1'
#                 stack+='0'
#             else:
#                 stack+=res3
#             # calcular con el carry 
#         print(stack)

# Solution().addBinary('11','1')


class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a)-1
        j = len(b)-1

        carry = 0 # 0 es false entonces okay 
        result = []

        while i >= 0 or j>=0 or carry:

            x = int(a[i]) if i>=0 else 0
            y = int(b[j]) if j>=0 else 0

            total = x + y + carry

            result.append(str(total%2))
            carry  = total //2

            i -=1
            j-=1

        return ''.join(result[::-1])


re= Solution().addBinary('1010','1011')

print(re)

