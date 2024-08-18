from os import remove

def main():

    task_list = list()

    while True:
        print(task_list)
        user_input = input(">").lower()     # takes user input
        if user_input == "/help":
            print("do \n/add to add a task.\n/rm to remove a task. \n/quit to quit the application.")
        elif user_input == "/quit":
            break
        elif user_input == "/add":    # adds a task to tasks list
            add_user_task_to_list = input(">>")
            task_list.append(f"{len(task_list) + 1}. {add_user_task_to_list}")
        elif user_input == "/rm": # removes a task
            task_number_to_remove = int(input("enter the task number to remove the task\n>>"))
            task_list.pop(task_number_to_remove - 1)
        else:
            print("do \n/add to add a task.\n/rm to remove a task. \n/quit to quit the application.")

if __name__ == '__main__':
    main()



