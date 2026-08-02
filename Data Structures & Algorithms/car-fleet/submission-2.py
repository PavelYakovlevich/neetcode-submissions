class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        cars.sort()
        stack = []

        for car in cars:
            while stack and stack[-1][1] <= car[1]:
                stack.pop()
            
            stack.append(car)
        
        return len(stack)


        