### Overview
* A decorator takes a function, add some functionality and returns it.
* Metaprogramming: the program tries to modify another part of the program at compile time.
* @symbol: func=adecorator(func)
* Multiple, order matters 

```Python
def adecorator(func):
    def inner(*args, **kwargs):
        print('decorating')
        func(*args, **kwargs)

    return inner

@adecorator
@adecorator
def func():
    print("func")

func()
```

### Reference
* [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
