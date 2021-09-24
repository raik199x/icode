import os


def clear_console():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)


def enter_continue():
    print("press enter to continue")
    enter = input()


def are_you_sure():
    print("are you sure you want to delete this?\n1. Yes 2. No\noption: ", end='')
    check = input()
    if check == '1':
        return '1'
    else:
        return '0'


def check_write_int():
    to_check = -1
    while to_check == -1:
        try:
            to_check = int(input())
        except Exception:
            print("get wrong data!")
            to_check = -1
        else:
            return to_check
