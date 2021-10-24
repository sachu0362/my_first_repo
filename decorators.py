def my_decorator(func):
    def wrap_func(*args,**kwargs):       #This syntax from line 1 to 6 is why the decorators are so powerful.
        print("*********")
        func(*args,**kwargs)
        print("*********")
    return wrap_func


@my_decorator
def hello(greeting,emoji):
    print(greeting,emoji)




hello('Namaste', ':-)')

'''
Thus this function (my_decorator) enhances the 
functionality of the hello() function here.
We can add anything under the wrap_func

Decorators supercharges the function which are
called after the decorators. e.g above

Thus decorators any any function which :
1. Accepts another function as an argument.
2. Have a wrapper function
3. Calling another function
4. Returning a function

'''
