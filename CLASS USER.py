class User:
    def __init__(self, first_name, last_name, course, year_level, section, username, password, pin_code):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.section = section
        self.username = username
        self.password = password
        self.pin_code = pin_code

def register_user():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    course = input("Enter your course: ")
    year_level = input("Enter your year level: ")
    section = input("Enter your section: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    pin_code = input("Enter your pin code (max 8 digits): ")

    while len(pin_code) > 8:
        print("Pin code should not exceed 8 digits. Please try again.")
        pin_code = input("Enter your pin code (max 8 digits): ")

    user = User(first_name, last_name, course, year_level, section, username, password, pin_code)
    print("Congratulations! You have successfully registered.")
    return user

def login_user(user):
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == user.username and password == user.password:
            while True:
                pin_code = input("Enter your pin code: ")
                if pin_code == user.pin_code:
                    print("Login successful!")
                    print("Your registered information:")
                    print(f"Name: {user.first_name} {user.last_name}")
                    print(f"Course: {user.course}")
                    print(f"Year Level: {user.year_level}")
                    print(f"Section: {user.section}")
                    break
                else:
                    print("Incorrect pin code. Please try again.")
        else:
            print("Incorrect username or password. Please try again.")

def main():
    user = register_user()
    while True:
        choice = input("Do you want to log in? (yes/no): ")
        if choice.lower() == "yes":
            login_user(user)
            break
        elif choice.lower() == "no":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()