class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, n: int) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        rank1, rank2 = self.rank[p1], self.rank[p2]
        if rank1 > rank2:
            self.par[p2] = p1
        elif rank1 < rank2:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        uf = UnionFind(n)

        for src, dst in edges:
            if not uf.union(src, dst):
                return False
        
        return True