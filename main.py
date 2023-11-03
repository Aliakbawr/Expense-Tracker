import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')

# Create a table for storing user information
conn.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY NOT NULL,
             password TEXT NOT NULL,
             last_login TEXT);''')


# Sign up function
def signup():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    conn.execute(f"INSERT OR IGNORE INTO users (username, password,last_login) VALUES ('{username}', '{password}', NULL)")
    conn.commit()
    print('Account created successfully!')
    user_panel(username)
    starter()


# Sign in function
def signin():
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    cursor = conn.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    if len(cursor.fetchall()) > 0:
        print('Login successful!')
        # Update the database with the login time
        conn.execute(f"UPDATE users SET last_login=datetime('now') WHERE username='{username}'")
        conn.commit()
        user_panel(username)

    else:
        print('Invalid username or password')
        starter()


def starter():
    while True:
        print('1. Sign up')
        print('2. Sign in')
        choice = input('Enter your choice: ')
        if choice == '1':
            signup()
        elif choice == '2':
            signin()
        else:
            print('Invalid choice')


def go_dutch_panel():
    print('Select:\n1)')


def user_panel(username):
    user_input = int(input('Select:\n1)\t2)Go Dutch!\t3)Business-Owner\t4)Sign out'))
    match user_input:
        case 1:
            print('Choose a plan:\n1)Envelope')
        case 2:
            print('Go Dutch!')
            go_dutch_panel()
        case 3:
            print('Choose a plan:\n1)Envelope')
        case 4:
            print('Returning ...')
            starter()
        case _:
            print('Wrong input')
            user_panel(username)


starter()
