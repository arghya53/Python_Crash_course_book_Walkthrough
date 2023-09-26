import json

def get_stored_username():
    '''Get stored username if available '''
    
    file_name = 'my_name.json'

    try:
        with open(file_name) as f:
            my_name = json.load(f)
    
    except FileNotFoundError:

        return None
    else:
        return my_name
    
def get_new_username():
    """ Prompt for a new username """

    my_name = input('What is your name?')
    file_name = 'my_name.json'

    with open(file_name, 'w') as f:
        json.dump(my_name, f)
    
    return my_name 

def greet_user():
    '''Greet the user '''

    my_name = get_stored_username()

    if my_name:
        print(f'Welcome {my_name}')

    else:

        my_name = get_new_username()
        print(f'You will be remembered when you come {my_name}')

greet_user()
    







