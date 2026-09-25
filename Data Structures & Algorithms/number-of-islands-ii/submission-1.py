class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = {}
        self.count = 0

    def add(self, pos: tuple):
        if pos not in self.par:
            self.par[pos] = pos
            self.rank[pos] = 0
            self.count += 1
    
    def find(self, pos: tuple) -> tuple:
        p = self.par[pos]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p

    def union(self, pos1: tuple, pos2: tuple) -> bool:
        p1, p2 = self.find(pos1), self.find(pos2)
        if p1 == p2:
            return False
        
        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 > r2:
            self.par[p2] = p1
        elif r2 > r1:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        self.count -= 1
        return True

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind()
        res = []
        for r, c in positions:
            pos = (r, c)
            if pos in uf.par:
                res.append(uf.count)
                continue
            uf.add(pos)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (r + dr, c + dc)
                if neighbor in uf.par:
                    uf.union(pos, neighbor)
            res.append(uf.count)
        
        return res