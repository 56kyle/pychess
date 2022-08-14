
from functools import wraps
from typing import Callable


def callback(func, before: Callable = None, after: Callable = None):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if before is not None:
            before(*args, **kwargs)
        return_value = func(*args, **kwargs)
        if after is not None:
            after(return_value)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper
