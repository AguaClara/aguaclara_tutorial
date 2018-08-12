# Define global variables.
all_todos_correct = True

def check_all_todos(printed_lines):
    global all_todos_correct

    print('Checking your code...')
    check_todo_1(printed_lines)
    check_todo_2(printed_lines)

    if(all_todos_correct):
        print('\nCongratulations, all of your TODO\'s are correct!')
        print('You can now proceed with the next tutorial section.\n')
    else:
        print('\nOops, not all of your TODO\'s are correct!')
        print('Check the above statements to see what you need to fix.\n')

def check_todo_1(printed_lines):
    global all_todos_correct

    if(printed_lines[0].lower() == 'rice and beans\n'):
        print('TODO 1 is correct.')
    else:
        all_todos_correct = False
        print('TODO 1 is correct.')

def check_todo_2(printed_lines):
    global all_todos_correct

    if(printed_lines[1] == '245\n'):
        print('TODO 2 is correct.')
    else:
        all_todos_correct = False
        print('TODO 2 is incorrect.')