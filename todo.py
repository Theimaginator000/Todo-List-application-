import os

import json

DATA_FILE = "todos.json"

def load_todos():

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE, "r") as file:

            todos = json.load(file)

        return todos

    return []

def save_todos(todos):

    with open(DATA_FILE, "w") as file:

        json.dump(todos, file)

def print_todos():

    todos = load_todos()

    if not todos:

        print("No todos.")

    else:

        print("Todo List:")

        for index, todo in enumerate(todos, start=1):

            print(f"{index}. {todo}")

def add_todo():

    todo = input("Enter a new todo: ")

    todos = load_todos()

    todos.append(todo)

    save_todos(todos)

    print("Todo added.")

def delete_todo():

    print_todos()

    choice = input("Enter the number of the todo to delete: ")

    todos = load_todos()

    if choice.isdigit():

        choice = int(choice)

        if 1 <= choice <= len(todos):

            todo = todos.pop(choice - 1)

            save_todos(todos)

            print(f"Todo '{todo}' deleted.")

            return

    print("Invalid choice.")

def main():

    while True:

        print()

        print("Todo List Application")

        print("---------------------")

        print("1. Print Todos")

        print("2. Add Todo")

        print("3. Delete Todo")

        print("4. Quit")

        choice = input("Enter your choice: ")

        

        if choice == "1":

            print_todos()

        elif choice == "2":

            add_todo()

        elif choice == "3":

            delete_todo()

        elif choice == "4":

            break

        else:

            print("Invalid choice. Please try again.")

if __name__ == "__main__":

    main()

