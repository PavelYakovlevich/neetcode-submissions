# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = []
        self.__curr = None

        self.__add_left_subtree(root)


    def next(self) -> int:
        self.__curr = self.__stack.pop()

        curr = self.__curr

        if curr.right:
            self.__add_left_subtree(curr.right)
        
        return self.__curr.val


    def hasNext(self) -> bool:
        return len(self.__stack) > 0
    
    def __add_left_subtree(self, curr: Optional[TreeNode]):
        if not curr:
            return
        
        while curr:
            self.__stack.append(curr)
            curr = curr.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()