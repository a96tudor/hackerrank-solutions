def person_lister(f):
    def inner(people):
        ordered_people = sorted(people, key=lambda x: int(x[2]))
        to_print = []
        for person in ordered_people:
            to_print.append(f(person))
        return to_print
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
