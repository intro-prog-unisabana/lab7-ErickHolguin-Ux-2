from password_manager import add_login, change_password, encrypt_passwords_in_file


def main() -> None:
    """TODO: Parte 5 - programa principal interactivo."""

    filename = input("Enter the CSV file name:\n")
    encrypt_passwords_in_file(filename)

    while True:
        option = input("Options: (1) Change Password, (2) Add Password, (3) Quit:\n")

        if option == "1":
            parts = input("Enter the website and the new password:\n").split()
            if len(parts) < 2:
                print("Input is in the wrong format!")
                continue
            website, new_pass = parts[0], parts[1]
            if len(new_pass) < 12:
                print("Password is too short!")
                continue
            if change_password(filename, website, new_pass):
                print("Password changed.")
            else:
                print("Website not found! Operation failed.")

        elif option == "2":
            parts = input("Enter the website, username, and password:\n").split()
            if len(parts) < 3:
                print("Input is in the wrong format!")
                continue
            website, user, passwd = parts[0], parts[1], parts[2]
            if len(passwd) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, user, passwd)
            print("Login added.")

        elif option == "3":
            break
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()
