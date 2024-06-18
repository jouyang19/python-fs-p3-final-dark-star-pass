from db.user import User
from db.password import Password

user_id = None

def sign_up():
    new_username = input("Username: ")
    new_password = input("Password: ")
    User.create_table()
    user = User.create(new_username, new_password)
    global user_id
    user_id = user.id
    return main()

def log_in():
    username = input("Username: ")
    password = input("Password: ")
    User.create_table()
    user = User.find_by_name(username)
    if user:
        if password == user.password:
            global user_id
            user_id = user.id
            return user_dashboard()
    else:
        print("Wrong username or password")
        return log_in()
    
    
def view_vault():
    Password.create_table()
    for item in Password.find_all_by_user_id(user_id):
        print(item)
    print("""
    (1) View Entry
    (2) Edit Entry
    (3) Delete Entry
    (4) Go Back
    """)
    choice = input("select an option: ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4": 
        return user_dashboard()
    


def user_dashboard():
    print("""
    (1) Password Vault
    (2) Add Password
    (3) Search
    """)
    choice = input("select an option: ")
    if choice == "1":
        view_vault()
    elif choice == "2":
        title = input("Title: ")
        username = input("Username: ")
        password = input("Password: ")
        account = Password.create(title, username, password, user_id)
        print(account)
        return user_dashboard()
        
def password_vault():
    pass

def view_entry():
    pass

def main():

    print("Dark Star Pass Online")

    print("""
    (1) Log In
    (2) Sign Up
    """)

    done = False

    while not done:
        
        choice = input("select an option: ")
        if choice == "2":
            sign_up()
        elif choice == "1":
            log_in()

if __name__ == "__main__":
    main()