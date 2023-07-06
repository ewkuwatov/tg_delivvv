students = {'Temur Eshkuwatov': 23,
            'Mirshod Safarov': 24}

def add_student(student_name, student_age):
    students[student_name] = student_age
    return 'Ученик успешно добавлен!'
def remove_student(student_name):
    students.pop(student_name)
def get_student_info(student_name):
    return students.get(student_name)
def update_student_age(student_name, new_age):
    students[student_name] = new_age
def get_all_students():
    return students
def count_students():
    return f'Количество учеников: {len(students.keys())} человек'

while True:
    admin = input('Что хотите сделать? ')
    if admin.lower() == 'добавить ученика':
        name = input('Имя ученика: ')
        age = int(input('Возраст ученика: '))
        print(add_student(name, age))
    elif admin.lower() == 'удалить ученика':
        name = input('Имя ученика: ')
        print(remove_student(name))
    elif admin.lower() == 'данные ученика':
        name = input('Имя ученика: ')
        print(get_student_info(name))
    elif admin.lower() == 'изменит данные ученика':
        name = input('Имя ученика: ')
        age = int(input('Возраст ученика: '))
        print(update_student_age(name, age))
    elif admin.lower() == 'все ученики':
        print(get_all_students())
    elif admin.lower() == 'всего количество учеников':
        print(count_students())
