class TodoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, title, description):
        item = TodoItem(title, description)
        self.items.append(item)

    def remove_item(self, index):
        if index >= 0 and index < len(self.items):
            del self.items[index]

    def mark_item_as_completed(self, index):
        if index >= 0 and index < len(self.items):
            self.items[index].completed = True

    def display_items(self):
        for index, item in enumerate(self.items):
            status = "Completed" if item.completed else "Not Completed"
            print(f"{index + 1}. {item.title} - {item.description} ({status})")

def main():
    todo_list = TodoList()

    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. Mark item as completed")
        print("4. Display items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title: ")
            description = input("Enter the description: ")
            todo_list.add_item(title, description)
        elif choice == "2":
            index = int(input("Enter the number of the item to remove: ")) - 1
            todo_list.remove_item(index)
        elif choice == "3":
            index = int(input("Enter the number of the item to mark as complete: ")) - 1
            todo_list.mark_item_as_completed(index)
        elif choice == "4":
            todo_list.display_items()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()