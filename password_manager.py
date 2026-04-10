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
        lector = csv.reader(file)
        rows = []
        for row in lector:
            if not row:   
                continue
            if row[0] != "website":
                row[2] = caesar_encrypt(row[2])
            rows.append(row)
            print(row)
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    return rows


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]

    found = False
    for i, row in enumerate(rows):
        if i == 0:  # saltar encabezado
            continue
        if row[0] == website:
            row[2] = caesar_encrypt(password)
            found = True
            break

    if not found:
        return False

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    return True


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    
    encrypted_password = caesar_encrypt(password)

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website_name, username, encrypted_password])

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if row]

    for row in rows:
        print(row)

    return rows
