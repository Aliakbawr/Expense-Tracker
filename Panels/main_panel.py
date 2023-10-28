def user_plan_chooser(user):
    user_input = int(input('Which describes you better:\n1)Beginner\t2)Serious Budgeter\t3)Business-Owner'))
    match user_input:
        case 1:
            print('Choose a plan:\n1)Envelope')
        case 2:
            print('Choose a plan:\n1)Envelope')
        case 3:
            print('Choose a plan:\n1)Envelope')
        case 4:
            print('Returning ...')
        case _:
            print('Wrong input')
            user_plan_chooser()

