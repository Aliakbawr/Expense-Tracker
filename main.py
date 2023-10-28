from Panels.main_panel import user_plan_chooser
from User.User import User


def starter():
    user_input = input('Enter the username:')
    password_input = input('Enter the password:')
    if user_input == 'a':
        if password_input == '1':
            print('successful login')
            user_plan_chooser(user)
        else:
            print('incorrect password')
    else:
        print('user not found')


user = User('a', '1')
print(user.name)
starter()
