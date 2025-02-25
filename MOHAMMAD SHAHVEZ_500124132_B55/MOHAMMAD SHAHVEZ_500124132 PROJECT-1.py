import os
import matplotlib.pyplot as plt
import numpy as np

def add_names():
    if not os.path.exists('totnumb.txt'):
        with open('totnumb.txt', 'w') as file:
            file.write('0')

    with open('namet.txt', 'a') as file:
        name = input('Enter your name: ')
        sapid = input('Enter your sapid: ')
        file.write(f"{name},{sapid}\n")
    with open('attennum.txt', 'a') as file1:
        file1.write('0\n')

def search_names():
    try:
        with open('totnumb.txt', 'r') as file:
            x = int(file.read())

        with open('namet.txt', 'r') as file:
            lines = [line.strip() for line in file]

        with open('attennum.txt', 'r') as file:
            lines1 = [line.strip() for line in file]

        a = input('Enter name or sapid: ')
        count = 0

        for i in lines:
            count += 1
            nas = i.strip().split(',')
            if a in nas:
                break

        print(f'NAME:- {nas[0]}\nSAPID:- {nas[1]}\nATTENDANCE:- {lines1[count - 1]} OUT OF {x}')

    except Exception as var:
        print(f'ERROR: {var}')

def mark_att():
    try:
        with open('totnumb.txt', 'r') as file:
            a = int(file.read())

        with open('totnumb.txt', 'w') as file:
            file.write(str(a + 1))

        with open('namet.txt', 'r') as file:
            names = [line.strip() for line in file]

        with open('attennum.txt', 'r') as file:
            attendances = [line.strip() for line in file]

        new_attendances = []

        for name, attendance in zip(names, attendances):
            while True:
                decision = input(f'{name}: Press P for Present, A for Absent: ').strip().upper()
                if decision in ('P', 'A'):
                    break
                else:
                    print('Invalid input. Please enter P for Present or A for Absent.')

            if decision == 'P':
                new_attendances.append(str(int(attendance) + 1))
            else:
                new_attendances.append(attendance)

        with open('attennum.txt', 'w') as file:
            for att in new_attendances:
                file.write(f'{att}\n')

    except Exception as e:
        print(f'ERROR: {e}')

def debarlist():
    try:
        with open('totnumb.txt', 'r') as file:
            a = int(file.read())

        with open('namet.txt', 'r') as file:
            lines = [line.strip() for line in file]

        with open('attennum.txt', 'r') as file:
            lines1 = [line.strip() for line in file]

        debarlist1 = []
        for i in range(len(lines)):
            x = int(lines1[i])
            if ((x / a) * 100) < 75:
                print(lines[i])
                debarlist1.append(lines[i])
                print((x / a) * 100)

        with open('debarlist.txt', 'w') as file:
            for i in debarlist1:
                file.write(f'{i}\n')

    except Exception as e:
        print(f'ERROR: {e}')

def plot_attendance():
    try:
        with open('totnumb.txt', 'r') as file:
            total_students = int(file.read())

        with open('namet.txt', 'r') as file:
            lines = [line.strip().split(',') for line in file]

        with open('attennum.txt', 'r') as file:
            attendances = [int(line.strip()) for line in file]

        names = [line[0] for line in lines]
        student_attendance = attendances
        total_attendance = [total_students] * len(names)

        # Plotting
        plt.figure(figsize=(12, 8))
        x = np.arange(len(names))
        width = 0.35

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, total_attendance, width, label='Total Attendance')
        rects2 = ax.bar(x + width/2, student_attendance, width, label='Individual Attendance')

        ax.set_xlabel('Students')
        ax.set_ylabel('Attendance')
        ax.set_title('Comparison of Total vs Individual Attendance')
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=45, ha='right')
        ax.legend()

        def autolabel(rects):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f'ERROR: {e}')

if __name__ == '__main__':
    while True:
        print('PRESS 1 FOR ADDING NAMES')
        print('PRESS 2 FOR MARKING ATTENDANCE')
        print('PRESS 3 FOR VIEWING ATTENDANCE')
        print('PRESS 4 FOR DEBAR LIST')
        print('PRESS 5 FOR PLOT ATTENDANCE')
        print('PRESS 6 FOR EXITING')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_names()
        elif choice == '2':
            mark_att()
        elif choice == '3':
            search_names()
        elif choice == '4':
            debarlist()
        elif choice == '5':
            plot_attendance()
        elif choice == '6':
            print('EXITED')
            break
        else:
            print('Please enter a valid option.')
            continue
