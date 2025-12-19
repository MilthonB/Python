from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ...

def sumar(lista, i):
    if i == len(lista):
        print("base -> 0")
        return 0

    print("bajo con:", lista[i])
    resultado = lista[i] + sumar(lista, i + 1)
    print("subo con:", resultado)
    return resultado


sumar([1,2,3],0)