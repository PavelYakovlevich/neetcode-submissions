class Solution:
    def isPathCrossing(self, path: str) -> bool:
        movs_directions = {
            'N': [0, -1],
            'S': [0, 1],
            'W': [-1, 0],
            'E': [1, 0]
        }

        pos = (0, 0)
        visit = set([pos])
        for direction in path:
            x_offset, y_offset = movs_directions[direction]
            pos = (pos[0] + x_offset, pos[1] + y_offset)
            if pos in visit:
                return True
            visit.add(pos)
        
        return False