#Homework Completion Tracker
total_homework = 4
original_homework = total_homework
print("Total homework assigned:", total_homework)

completed_homework = 0
task_number = 1

while completed_homework < total_homework:

    if task_number == 1:
        print("Task 1: Math homework")
    elif task_number == 2:
        print("Task 2: Science homework")
    elif task_number == 3:
        print("Task 3: History homework")
    elif task_number == 4:
        print("Task 4: English homework")

        answer = input("Have you completed this task? (yes/no):")

        if answer == "yes":
            completed_homework += 1
            print("Great job! You have completed", completed_homework, "homework tasks.")
                    
