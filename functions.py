FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Returns the files as read
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from todo")
