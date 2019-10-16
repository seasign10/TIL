def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('hahahahaha')
    return wrapper

@hello
def bye():
    print('bye bye')

bye()