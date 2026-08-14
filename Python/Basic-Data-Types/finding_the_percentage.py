student_marks = {}

for _ in range(int(input())):
    name, *line = input().split()
    student_marks[name] = list(map(float, line))

query_name = input()
print(f"{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}")
