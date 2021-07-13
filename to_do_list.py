#In this assignment you are going to create a TODO app. When the app starts it should present user with the following menu:
#Press 1 to add task
#Press 2 to delete task (HARD MODE)
#Press 3 to view all tasks
#Press q to quit
#The user should only be allowed to quit when they press 'q'.
#Add Task:
#Ask the user for the 'title' and 'priority' of the task. Priority can be high, medium and low.
#Delete Task: (HARD MODE)
#Show user all the tasks along with the index number of each task. User can then enter the index number of the task to delete the task.
#View all tasks:
#Allow the user to view all the tasks in the following format:
#1 - Wash the car - high
#2 - Mow the lawn - low
#Store each task in a dictionary and use 'title' and 'priority' as keys of the dictionary.
#Store each dictionary inside an array. Array will represent list of tasks.
#** HINT **
#tasks = [] # global array
#input("Enter your option")

tasks = [] #global array

def view_tasks():
    print(tasks)


while True:
    print("Please make a choice from the following menu:")
    print("1 - Add Task")
    print("2 - Delete Task")
    print("3 - View all tasks ")
    print("q to quit")

    choice = input("Enter Choice:")

    if choice == "q":
        break

    if choice == "1":
        title = input("Please enter a task title:")
        priority = input("Please enter priority : high, medium or low - ")
        task = {"title": title, "priority": priority}
        tasks.append(task)

    if choice == "2":
        view_tasks()
        del_task = int(input("Chose a task to delete:" ))
        del tasks[del_task - 1]
        view_tasks()


    if choice == "3": 
        view_tasks()

print(tasks)