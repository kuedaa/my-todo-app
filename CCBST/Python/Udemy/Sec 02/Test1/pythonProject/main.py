#from functions import get_todos, write_todos
import time
import functions

now = time.strftime('%b %d, %Y %H:%M:%S')
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') :
        todo = user_action[4:]  + "\n"

        todos = functions.get_todos()  # filepath is argument and 'Files/.todos.txt' is argument value
        todos.append(todo)

        functions.write_todos(todos, )

    elif user_action.startswith('show') :
        todos = functions.get_todos()

        for index, item in enumerate(todos) :
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)
    elif user_action.startswith('edit') :
        try:
            number = int(user_action[5:])
            number = number -1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number]= new_todo + '\n'

            functions.write_todos(todos, )
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete') :
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            todo_to_remove = todos[number-1].strip('\n')
            todos.pop(number-1)

            functions.write_todos(todos, )

            print(f"Todo {todo_to_remove} was remove from the list.")
        except IndexError:
            print('There is not item with this number.')
            continue

    elif user_action.startswith('exit') :
        break
    else:
        print('The command is not valid!')

print('Bye!')