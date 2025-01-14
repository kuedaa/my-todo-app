#Beginning a program
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action :
        todo = user_action[4:]  #+ "\n"

        with open('Files/.todos.txt', 'r') as file :
            todos =file.readlines()

        todos.append(todo)

        with open('Files/.todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action :
        with open('Files/.todos.txt', 'r') as file :
            todos = file.readlines()

        for index, item in enumerate(todos) :
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif 'edit' in user_action :
        number = int(user_action[5:])
        number = number -1

        with open('Files/.todos.txt', 'r') as file :
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number]= new_todo + '\n'

        with open('Files/.todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action :
        with open('Files/.todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(user_action[9:])
        todo_to_remove = todos[number-1].strip('\n')
        todos.pop(number-1)

        with open('Files/.todos.txt', 'w') as file:
            file.writelines(todos)

        print(f"Todo {todo_to_remove} was remove from the list.")

    elif 'exit' in user_action :
        break
    else:
        print('The command is not valid!')

print('Bye!')