
import TodoFunctions
import time
now = time.strftime("%b %d. %Y %H:%M:%S")
print("It is :",now)
while True:
    user_action  = input("Add, show, edit, complete :")
    user_action = user_action.strip()


    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action.strip('add ') + '\n'
        # file = open('todos.txt','r')
        # todos = file.readlines()
        # file.close()
        print(f"added: {todo}")
        todos = TodoFunctions.get_todos()
        todos.append(todo)
        TodoFunctions.write_todos(todos_arg= todos)

    elif user_action.startswith("show"):
        #     file = open('todos.txt','r')
        #     todos = file.readlines()
        #     file.close()
        todos = TodoFunctions.get_todos()
        # new_todos = []
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
        # print(todos)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:6])
            new_todo = user_action[7:]
            print(f"Edited no: {number} to {new_todo}")
            number = number - 1
            todos = TodoFunctions.get_todos()

            todos[number] = new_todo + '\n'
            # print("here is the new list",todos)
            # file.writelines(todos)
            TodoFunctions.write_todos(todos_arg= todos)
        except:
            print("checck command, plz try again")
            continue

    elif 'completed' in user_action or 'delete' in user_action:
        try:
            if 'completed' in user_action:
                number = int(user_action[10:])
            else:
                number = int(user_action[7:])
            todos = TodoFunctions.get_todos()
            removed = todos[number - 1].strip('\n')
            print(f"Todo: '{removed}' was removed")
            todos.pop(number - 1)
            TodoFunctions.write_todos(todos_arg= todos)
        except:
            print("Invalid input, please try again")
            continue

    elif user_action.startswith("exit"):
        print("thank you ")
        break


    elif user_action.startswith("help"):
        print("\nFunction suffix followed by the parameter...")
        print("     for adding: add (new reminder) ")
        print("     for editing: edit (number of the old reminder) (new reminder) ")
        print("     For completion, completed (index of the reminder).")
        print("     ie: 'add finish maths homework by this evening.' ")

    else:
        print("Not valid, please retry ")

