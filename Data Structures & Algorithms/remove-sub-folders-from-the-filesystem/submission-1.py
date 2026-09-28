# class TrieNode:
#     def __init__(self, folder: str = ''):
#         self.children = {}
#         self.folder = folder
#         self.sub_folders = 0

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def add(folder: str) -> bool:
#         parts = folder.split('/')
#         node = self.root
#         for part in parts:
#             if part not in node.children:
#                 node.children[part] = TrieNode(part)
#             else node = 

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        folders = set()

        for fol in folder:
            parts = fol.split('/')
            is_subfolder = False

            for i in range(1, len(parts)):
                prefix = '/'.join(parts[:i+1])
                if prefix in folders:
                    is_subfolder = True
                    break
                    
            if not is_subfolder:
                folders.add(fol)
        
        return list(folders)
