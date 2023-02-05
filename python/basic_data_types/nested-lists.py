if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students = sorted(students, key=lambda x: x[1])

    min_score = students[0][1]
    idx = 0

    while students[idx][1] == min_score:
        idx += 1

    second_min_score = students[idx][1]
    to_print = []
    while idx < len(students) and students[idx][1] == second_min_score:
        to_print.append(students[idx][0])
        idx += 1

    print('\n'.join(x for x in sorted(to_print)))
