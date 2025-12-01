n = int(input())
students = []

for i in range(n):
    surname = input()
    name = input()
    class_ = input()
    birthdate = input()
    students.append((class_, surname, name, birthdate))

students.sort(key=lambda x: (int(x[0][:-1]), x[0][-1], x[1]))
for class_, surname, name, birthdate in students:
    print(class_, surname, name, birthdate)