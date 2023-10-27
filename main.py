user_input = input('Enter the username:')
password_input = input('Enter the password:')

if user_input == 'admin':
    if password_input == 'admin':
        print('successful login')
    else:
        print('incorrect password')
else:
    print('user not found')
