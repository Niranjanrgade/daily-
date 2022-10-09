if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key in student_marks:
        total_marks = 0
        if key == query_name:
            for score in student_marks[key]:
                total_marks += score
            avg = (total_marks / len(student_marks[key]))
            print(f"{avg:.2f}")
