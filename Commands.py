from Phone_book import Record, AddressBook
import pickle
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Contact/s don't exist"
        except KeyError:
            return "You don't have this phone in your contacts"

    return inner

def parse_input(user_input):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, book: AddressBook):

    if len(args) < 2:
        return "Please provide both name and phone number."
    name, phone = args
    if len(phone) != 10 or not phone.isdigit():
        return "Phone number must be 10 digits."

    record = book.find(name)
    if not record:
        record = Record(name)
        book.add_record(record)
        record.add_phone(phone)
        return f"Contact {name} added with phone {phone}."
    else:
        record.add_phone(phone)
        return f"Phone {phone} added to contact {name}."

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return f"Phone for {name} updated."
    raise KeyError
@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        phones = ", ".join(phone.value for phone in record.phones)
        return f"{name}: {phones}"
    return "Contact not found."

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Give me name and birthday"

    name, birthday = args
    record = book.find(name)
    if not record:
        return f"Contact {name} not found."

    try:
        record.add_birthday(birthday)
    except ValueError:
        return "Give me name and birthday"

    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday.value}."
    return f"No birthday set for {name}."

def birthdays(args, book: AddressBook):
    days = int(args[0]) if args else 7
    upcoming = book.get_upcoming_birthday(days)
    if not upcoming:
        return "No birthdays in the next week."

    result = []
    for entry in upcoming:
        result.append(f"{entry['name']} - {entry['congratulation_date']}")
    return "\n".join(result)

@input_error
def show_all(book: AddressBook):
    if not book.data:
        raise IndexError("No contacts in the address book.")

    result = []
    for name, record in book.data.items():
        phones = ", ".join(phone.value for phone in record.phones)
        result.append(f"{name}: {phones}, {record.birthday.value if record.birthday else ""}")
    return "\n".join(result)

def save_data(book: AddressBook, filename):
    with open(filename, "wb") as f:
        return pickle.dump(book, f)

def load_data(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

