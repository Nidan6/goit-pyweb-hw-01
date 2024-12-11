from Commands import parse_input, add_contact, change_contact, show_all, show_phone, add_birthday, show_birthday, birthdays, save_data, load_data
from UI import  ConsolUI

def main():
    ui = ConsolUI()
    book = load_data(filename="addressbook.pkl")
    ui.display_massage("Welcome to the assistant bot!")


    while True:
        user_input = ui.user_input("Enter a command: ")
        command, args = parse_input(user_input)

        if command is None:
            ui.display_massage("Please enter a command.")
            continue

        if command in ["close", "exit"]:
            ui.display_massage("Good bye!")
            save_data(book, filename="addressbook.pkl")
            break

        elif command == "hello":
            ui.display_massage("How can I help you?")

        elif command == "add":
            ui.display_massage(add_contact(args, book))

        elif command == "change":
            ui.display_massage(change_contact(args, book))

        elif command == "phone":
            ui.display_massage(show_phone(args, book))

        elif command == "all":
            ui.show_contacts(show_all(book))

        elif command == "add-birthday":
            ui.display_massage(add_birthday(args, book))

        elif command == "show-birthday":
            ui.show_birthdays(show_birthday(args, book))

        elif command == "birthdays":
            ui.display_massage(birthdays(args, book))

        elif command == "help":
            ui.show_help(["exit", "hello", "add", "change", "phone", "all", "add-birthday", "show-birthday", "birthdays"])

        else:
            ui.display_massage("Invalid command, type 'help' to see all commands")


if __name__ == "__main__":
    main()