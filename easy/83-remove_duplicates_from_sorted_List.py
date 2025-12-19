from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        retorno = dummy

        while head:
            # si aún no he agregado ningún nodo real
            if retorno == dummy:
                retorno.next = ListNode(head.val)
                retorno = retorno.next

            # si ya hay nodos reales, comparo contra el último agregado
            elif head.val != retorno.val:
                retorno.next = ListNode(head.val)
                retorno = retorno.next

            head = head.next

        return dummy.next


n1 = ListNode(0)
n2 =  ListNode(0)
n3 =  ListNode(0)
n4 =  ListNode(0)
n5 =  ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# print(n1.next.val)


re =  Solution().deleteDuplicates(n1)

while re:
    print(re.val)
    re = re.next

