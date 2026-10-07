import string
import datetime


# Functions

def encode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    encoded_text = ""

    for char in input_text:
        lower_char = char.lower()

        if lower_char in alphabet:
            old_index = alphabet.index(lower_char)
            new_index = (old_index + shift) % 26
            encoded_text += alphabet[new_index]
        else:
            encoded_text += char

    return alphabet, encoded_text


def decode(input_text, shift):
    alphabet = list(string.ascii_lowercase)
    decoded_text = ""

    for char in input_text:
        lower_char = char.lower()

        if lower_char in alphabet:
            old_index = alphabet.index(lower_char)
            new_index = (old_index - shift) % 26
            decoded_text += alphabet[new_index]
        else:
            decoded_text += char

    return decoded_text

# BankAccount

class BankAccount:

    def __init__(
        self,
        name="Rainy",
        ID="1234",
        creation_date=datetime.date.today(),
        balance=0
    ):

        if type(creation_date) is not datetime.date:
            raise Exception("creation_date must be a datetime.date")

        if creation_date > datetime.date.today():
            raise Exception("creation_date cannot be in the future")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):

        if amount < 0:
            print(self.balance)
            return self.balance

        self.balance += amount

        print(self.balance)

        return self.balance

    def withdraw(self, amount):

        if amount < 0:
            raise Exception("Withdrawal amount cannot be negative")

        self.balance -= amount

        print(self.balance)

        return self.balance

    def view_balance(self):

        print(self.balance)

        return self.balance


# SavingsAccount

class SavingsAccount(BankAccount):

    def withdraw(self, amount):

        account_age = (
            datetime.date.today() - self.creation_date
        ).days

        if account_age < 180:
            print(self.balance)
            return self.balance

        if amount > self.balance:
            print(self.balance)
            return self.balance

        if amount < 0:
            print(self.balance)
            return self.balance

        self.balance -= amount

        print(self.balance)

        return self.balance


# CheckingAccount

class CheckingAccount(BankAccount):

    def withdraw(self, amount):

        if amount < 0:
            raise Exception("Withdrawal amount cannot be negative")

        self.balance -= amount

        if self.balance < 0:
            self.balance -= 30

        print(self.balance)

        return self.balance