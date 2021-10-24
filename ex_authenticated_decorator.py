# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrap_func(*args):
        if user1['valid']:
            fn(args)
            return
        print('Authentication Failure....!!!')

    return wrap_func


@authenticated
def message_friends(user):
    print('Message has been sent successfully ')


message_friends(user1)
