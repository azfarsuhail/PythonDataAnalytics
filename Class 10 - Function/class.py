# from typing import Callable

# def my_decorator(func:Callable[[],None]) -> Callable[[],None]:
#     def wrapper()-> None:
#         print("Something is happening before the fucntion is called")
#         func()
#         print("Something is happening after the function is called")
#         return wrapper
    
# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

# from typing import Callable

# def my_decorator(func: Callable[..., Callable[..., None]]) -> Callable[..., None]:
#     def wrapper() -> None:
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

from typing import Callable

def my_decorator(func: Callable[..., Callable[..., None]]) -> Callable[..., None]:
    def wrapper(*args, **kwargs) -> None:
        print("Something is happening before the function is called")
        func(*args, **kwargs)
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello(number: int):
    print("Hello, the number is:", number)

say_hello(42)
