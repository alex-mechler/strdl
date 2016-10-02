import inspect
import importlib


def parse(file):
    module = importlib.import_module(file.name.strip('.py'))
    print(module.__doc__)
    function_list = inspect.getmembers(module, inspect.isfunction)
    for function in function_list:
        print(getattr(module, function[0]).__doc__)
