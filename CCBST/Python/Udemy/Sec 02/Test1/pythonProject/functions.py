FILEPATH = 'Files/.todos.txt'

def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of to-do
    items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write a the list of to-do list in a file file."""
    with open(filepath, 'w') as filelocal:
        filelocal.writelines(todos_arg)

