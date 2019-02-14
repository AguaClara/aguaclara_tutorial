def test_todos(printed_lines):
    if(all_todos_correct(printed_lines)):
        print('\nCongratulations, all of your TODO\'s are correct!')
        print('You can now proceed with the next tutorial section.\n')
    else:
        print('\nOops, not all of your TODO\'s are correct!')
        print('Check the above statements to see what you need to fix.\n')

def all_todos_correct(printed_lines):
    all_correct = True
    correct_answers = [
        'rice and beans',
        '245',
        '[\'flocculation\', \'1 lps\', \'filtration\']',
        'power bacon',
        'no',
        '265252859812191058636308480000000',
        '340282366920938463463374607431768211456'
    ]

    print('Testing your code...')
    for todo_number in range(7):
        expected = correct_answers[todo_number]
        actual = printed_lines[todo_number].lower()[:-1] # Remove extra \n.

        if(expected == actual):
            print('TODO ' + str(todo_number + 1) + ' is correct.')
        else:
            all_correct = False
            print('TODO ' + str(todo_number + 1) + ' is incorrect.')
    
    return all_correct