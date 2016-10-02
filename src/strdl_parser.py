import inspect
import importlib
import strdl_struct


def parse(file):
    filename = file.name.strip('.py')
    module = importlib.import_module(filename)
    module_doc = module.__doc__
    function_list = inspect.getmembers(module, inspect.isfunction)
    functs = []
    for function in function_list:
        funct_string = getattr(module, function[0]).__doc__
        params = get_params(funct_string)
        functs.append(strdl_struct.strdl_method(function[0], params))
    return strdl_struct.strdl_struct(filename, module_doc, functs)


def get_params(funct_string) -> list:
        funct_string.strip()
        functs = []
        for line in funct_string.split('\n'):
            line.strip()
            if 'param' in line:
                split = line.split(' ')
                print(split)
                docs = ''
                for i in range(6, len(split)):
                    docs += split[i] + ' '
                functs.append(strdl_struct.strdl_param(split[5].strip(':'), docs))
        return functs
