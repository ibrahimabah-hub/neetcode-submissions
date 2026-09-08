class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        loop = 0
        while(len(students)>0 and loop!=len(students)):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                loop=0
            else:
                student = students[0]
                students.pop(0)
                students.append(student)
                loop+=1

        return(len(students))