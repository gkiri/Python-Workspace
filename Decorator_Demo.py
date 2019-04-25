from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee() #Ifyou call say_whee() after bed time nothing will happen
############################################################
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
    
say_whee()   
    
    
 So, @my_decorator is just an easier way of saying say_whee = my_decorator(say_whee). It’s how you apply a decorator to a function.

Source : https://realpython.com/primer-on-python-decorators/
