height = 176
age = 22
count_baby = 1
student_now = False

if 18 <= age <= 28:
    if count_baby >= 2:
        print('Grace period')
    elif student_now is True:
        print('Grace period')
    else:
        if height < 170:
            print('To tanksman')
        elif height < 185:
            print('To navy')
        elif height < 200:
            print('To special forces')
        else:
            print('Other forces')
else:
    print('Not proper age')
