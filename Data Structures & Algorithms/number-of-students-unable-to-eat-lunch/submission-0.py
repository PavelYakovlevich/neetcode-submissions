class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_sum = sum(students)
        while len(students) > 0 and len(sandwiches) > 0:
            if (students_sum == len(students) and sandwiches[0] == 0) or (students_sum == 0 and sandwiches[0] == 1):
                return len(students)

            if students[0] == sandwiches[0]:
                students_sum -= students[0]
                students.pop(0)
                sandwiches.pop(0)

            elif students[0] != sandwiches[0]:
                students.append(students.pop(0))
        
        return 0