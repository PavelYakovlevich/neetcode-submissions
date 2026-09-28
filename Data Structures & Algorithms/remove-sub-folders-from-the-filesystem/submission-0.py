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
            curr = ''
            is_subfolder = False
            for fol_part in fol[1:].split('/'):
                curr = curr + '/' + fol_part
                if curr in folders:
                    is_subfolder = True
                    break
            if not is_subfolder:
                folders.add(fol)
        
        return list(folders)
