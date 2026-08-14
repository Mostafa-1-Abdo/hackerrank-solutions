records = []

for _ in range(int(input())):
    records.append([input(), float(input())])

records.sort(key=lambda record: (record[1], record[0]))
lowest_score = records[0][1]

for record in records:
    if record[1] != lowest_score:
        second_lowest_score = record[1]
        break

second_lowest_score_records = []
for record in records:
    if record[1] == second_lowest_score:
        print(record[0])
