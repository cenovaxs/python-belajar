def decorator_function(original_function):
    def wrapper_function(*args):
        print('wrapper executed this before {}'.format(
            original_function.__name__))
        return original_function(*args)
    return wrapper_function


@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info('pujas', 33)
