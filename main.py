import time
from optiontal_func import *
from classes import *

students = list()
teachers = list()
subjects = list()
groups = list()


def exporting():
    file_students = open("students", "w+")
    file_teachers = open("teachers", "w+")
    file_subjects = open("subjects", "w+")
    file_groups = open("groups", "w+")
    for i in students:
        i.save_file(file_students)
    for i in teachers:
        i.save_file(file_teachers)
    for i in subjects:
        i.save_file(file_subjects)
    for i in groups:
        i.save_file(file_groups)


def importing():
    name = ''
    surname = ''
    age = 0
    group_number = ''
    plan = ''
    salary = 0
    try:
        file_students = open("students", "r")
    except Exception:
        pass
    else:
        data = file_students.read()
        data = data.replace("\n", ":").split(":")
        data.remove("")
        step = 0
        for i in data:
            if step == 0:
                name = i
            elif step == 1:
                surname = i
            elif step == 2:
                age = int(i)
            elif step == 3:
                group_number = i
            elif step == 4:
                plan = i
                step = 0
                students.append(Student(name, surname, age, group_number, plan))
            step += 1
        file_students.close()
    try:
        file_teachers = open("teachers","r")
    except Exception:
        pass
    else:
        data = file_teachers.read()
        data = data.replace("\n", ":").split(":")
        data.remove("")
        step = 0
        for i in data:
            if step == 0:
                name = i
            elif step == 1:
                surname = i
            elif step == 2:
                age = int(i)
            elif step == 3:
                salary = int(i)
            elif step == 4:
                objecte = i
                step = 0
                teachers.append(Student(name, surname, age, salary, objecte))
            step += 1
        file_teachers.close()
    try:
        file_subjects = open("subjects", "r")
    except Exception:
        pass
    else:
        data = file_subjects.read()
        data = data.split("\n")
        data.remove("")
        for i in data:
            subjects.append(Subject(i))
        file_subjects.close()
    try:
        file_groups = open("groups","r")
    except Exception:
        pass
    else:
        data = file_groups.read()
        data = data.split("\n")
        data.remove("")
        for i in data:
            groups.append(Group(i))
        file_groups.close()


def menu(variant):
    clear_console()
    if variant == 0:
        print("1. print menu")
        print("2. add menu")
        print("3. delete menu")
        print("10. exit program")
    elif variant == 1:
        print("11. print teachers")
        print("12. print students")
        print("13. print subjects")
        print("14. print groups")
        print("19. go back")
    elif variant == 2:
        print("21. add teachers")
        print("22. add students")
        print("23. add subjects")
        print("24. add groups")
        print("29. go back")
    elif variant == 3:
        print("31. delete teacher")
        print("32. delete student")
        print("33. delete subject")
        print("34. delete group")
        print("39 go back")
    print("choose option:", end=' ')


def create(who):
    clear_console()
    if who == 'teacher':
        print("Write name: ", end='')
        name = input()

        print("Write surname: ", end='')
        surname = input()

        print("Write age ", end='')
        age = check_write_int()

        print("Write salary: ", end='')
        salary = check_write_int()

        check = 0
        # check if we've got any subjects
        for _ in subjects:
            check += 1
            if check == 1:
                break
        if check == 0:
            print("subject not found, so skipped")
            subject = "none"
        else:
            print("choose subject:")
            for num, i in enumerate(subjects):
                print(str(num + 1), end=' ')
                i.subject_output()
            number = check_write_int()
            try:
                subject = subjects[number - 1].subject_name
            except IndexError:
                print("invalid subject, so skipped")
                subject = "none"

        teachers.append(Teacher(name, surname, age, salary, subject))

    elif who == 'student':
        print("Write name: ", end='')
        name = input()

        print("Write surname: ", end='')
        surname = input()

        print("Write age ", end='')
        age = check_write_int()

        print("choose education plane:\n1. Free\n2. Non-free")
        choose = 0
        while choose != 1 and choose != 2:
            choose = check_write_int()
        if choose == 1:
            education_plan = "Free"
        else:
            education_plan = "Non-free"

        checker = 0
        for _ in groups:
            checker += 1
        if checker == 0:
            print("groups weren't found, so skipped")
            group_number = "none"
            time.sleep(2)
        else:
            print("choose group:")
            for num, i in enumerate(groups):
                print(str(num + 1) + " ", end='')
                i.group_output()
            number = check_write_int()
            try:
                group_number = groups[number - 1].group_number
            except IndexError:
                print("invalid group, so skipped")
                group_number = "none"

        students.append(Student(name, surname, age, group_number, education_plan))
    elif who == 'subject':
        print("write name of subject: ", end='')
        subj = input()
        subjects.append(Subject(subj))
    elif who == 'group':
        print("write group number: ", end='')
        grp = input()
        groups.append(Group(grp))
    print("successfully added!")
    time.sleep(1)


def print_something(who):
    if who == 'teacher' or who == 'student':
        for num, i in enumerate(teachers):
            print(str(num + 1))
            i.output_info()
    elif who == 'student':
        for num, i in enumerate(students):
            print(str(num + 1))
            i.output_info()
    elif who == 'subject':
        for num, i in enumerate(subjects):
            print(str(num + 1) + " ", end='')
            i.subject_output()
    elif who == 'group':
        for num, i in enumerate(groups):
            print(str(num + 1) + " ", end='')
            i.group_output()


def delete(who):
    clear_console()
    if who == 'teacher':
        print_something('teacher')
        print("\nWrite number of item or 0 to go back")
        deleter = check_write_int()
        if deleter == 0:
            return
        try:
            clear_console()
            teachers[deleter - 1].output_info()
        except IndexError:
            print("invalid number, exit delete function...")
            time.sleep(1)
            return
        else:
            check = are_you_sure()
            if check != '1':
                print("exit delete function")
                time.sleep(1)
                return
            teachers.remove(teachers[deleter - 1])
            print("removed!")
            time.sleep(1)
    elif who == 'student':
        print_something('student')
        print("\nWrite number of item or 0 to go back")
        deleter = check_write_int()
        if deleter == 0:
            return
        try:
            clear_console()
            students[deleter - 1].output_info()
        except IndexError:
            print("invalid number, exit delete function...")
            time.sleep(1)
            return
        else:
            check = are_you_sure()
            if check != '1':
                print("exit delete function")
                time.sleep(1)
                return
            students.remove(students[deleter - 1])
            print("removed!")
            time.sleep(1)
    elif who == 'subject':
        print_something('subject')
        print("\nWrite number of item or 0 to go back")
        deleter = check_write_int()
        if deleter == 0:
            return
        try:
            clear_console()
            subjects[deleter - 1].subject_output()
        except IndexError:
            print("invalid number, exit delete function...")
            time.sleep(1)
            return
        else:
            check = are_you_sure()
            if check != '1':
                print("exit delete function")
                time.sleep(1)
                return
            subjects.remove(subjects[deleter - 1])
            print("removed!")
            time.sleep(1)
    elif who == 'group':
        print_something('group')
        print("\nWrite number of item or 0 to go back")
        deleter = check_write_int()
        if deleter == 0:
            return
        try:
            clear_console()
            groups[deleter - 1].group_output()
        except IndexError:
            print("invalid number, exit delete function...")
            time.sleep(1)
            return
        else:
            check = are_you_sure()
            if check != '1':
                print("exit delete function")
                time.sleep(1)
                return
            groups.remove(groups[deleter - 1])
            print("removed!")
            time.sleep(1)


def working():
    start = 1  # working flag
    while start == 1:
        menu(0)  # print menu
        option = check_write_int()
        if option == 10:  # end program
            start = 0
            continue
        elif option == 1:  # open print menu
            while option != 19:
                menu(1)
                option = check_write_int()
                clear_console()
                if option < 11 or option > 19 or (15 < option < 19):
                    print("invalid value!")
                    time.sleep(1)
                elif option == 11:
                    print_something('teacher')
                elif option == 12:
                    print_something('student')
                elif option == 13:
                    print_something("subject")
                elif option == 14:
                    print_something("group")
                elif option == 19:
                    break
                enter_continue()

        elif option == 2:
            while option != 29:
                menu(2)
                option = check_write_int()
                if option < 21 or option > 29 or (24 < option < 29):
                    print("invalid value!")
                    time.sleep(1)
                elif option == 21:
                    create('teacher')
                elif option == 22:
                    create('student')
                elif option == 23:
                    create("subject")
                elif option == 24:
                    create("group")
        elif option == 3:
            while option != 39:
                menu(3)
                option = check_write_int()
                if option < 31 or option > 39 or (34 < option < 39):
                    print("invalid value!")
                    time.sleep(1)
                elif option == 31:
                    delete('teacher')
                elif option == 32:
                    delete('student')
                elif option == 33:
                    delete("subject")
                elif option == 34:
                    delete("group")


if __name__ == '__main__':
    importing()
    working()
    exporting()
