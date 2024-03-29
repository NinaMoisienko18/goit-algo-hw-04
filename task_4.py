def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return f"Contact '{name}' added."
    else:
        return "Invalid input."


def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Contact '{name}' changed."
        else:
            return f"Contact '{name}' not found."
    else:
        return "Invalid input."


def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return f"Phone number for {name}: {contacts[name]}"
        else:
            return f"Contact '{name}' not found."
    else:
        return "Invalid input. Please provide the name."

def show_all(contacts):
    if not contacts:
        return "There are no contacts."

    result = "\n>>> All Contacts:\n"
    for name, number in contacts.items():
        result += f"{name}: {number}\n"

    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
