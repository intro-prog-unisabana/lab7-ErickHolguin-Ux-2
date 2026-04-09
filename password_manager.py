import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    
    with open(filename, 'r') as file:
        password = file.readline().strip()
    encrypted_password = caesar_encrypt(password)
    with open(filename, 'w') as file:
        file.write(encrypted_password)


def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
