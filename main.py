# TODO: display tasklist as default
# TODO: add a task
# TODO: remove a task
# TODO:


def main():

    task_list = list()

    while True:
        user_input = input(">").lower()     # takes user input
        if user_input == "/quit":
            break
        if user_input == "/add":    # adds a task to tasks list
            add_user_task_to_list = input(">>")
            task_list.append(f"{len(task_list) + 1}. {add_user_task_to_list}")
        if user_input == "/remove": # removes a task
            pass


        print(task_list)







if __name__ == '__main__':
    main()



