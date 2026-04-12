from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""

    filename = input("Enter the CSV file name:\n")
    encrypt_all_passwords(filename)


if __name__ == "__main__":
    main()
