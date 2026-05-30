class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_count = len(students)
        counter = Counter(students)

        for s in sandwiches:
            if counter[s] > 0:
                counter[s] -= 1
                students_count -= 1
            else:
                break
        
        return students_count