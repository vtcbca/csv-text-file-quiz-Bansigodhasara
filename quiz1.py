import csv
data = [
    ("1", "bansi", 5000),
    ("2", "om", 4000),
    ("3", "krishna", 6000),
    ("4", "radha", 5500),
    ("5", "sai", 4200)
]

with open("salary.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sid", "sname", "salary"])
    writer.writerows(data)
