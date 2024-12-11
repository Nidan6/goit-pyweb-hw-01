from abc import ABC, abstractmethod

class AbstractUI(ABC):

    @abstractmethod
    def display_massage(self, massage: str):
        pass

    @abstractmethod
    def user_input(self, inp: str):
        pass

    @abstractmethod
    def show_contacts(self, contacts: str):
        pass

    @abstractmethod
    def show_birthdays(self, birthdays: str):
        pass

    @abstractmethod
    def show_help(self, commands: list):
        pass

class ConsolUI(AbstractUI):

    def display_massage(self, massage: str):
        print(massage)

    def user_input(self, inp: str):
        return input(inp)

    def show_contacts(self, contacts: str):
        print(contacts)

    def show_birthdays(self, birthdays: str):
        print(birthdays)

    def show_help(self, commands: list):
        for command in commands:
            print(command)
