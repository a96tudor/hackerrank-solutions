from collections import namedtuple

if __name__ == '__main__':
    Student = namedtuple('Student', 'ID,MARKS,CLASS,NAME')

    n = int(input())
    columns = [x for x in input().split()]
    students = []

    for _ in range(n):
        data = input().split()

        students.append(Student(**{
            col: d for col, d in zip(columns, data)
        }))

    print(sum(int(student.MARKS) for student in students) / len(students))
