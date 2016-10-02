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
        funct_string = getattr(module, function[0]).__doc__.strip()
        params = get_params(funct_string)
        desc = get_desc(funct_string)
        ret = get_return(funct_string)
        functs.append(strdl_struct.strdl_method(function[0], desc, params, ret))
    return strdl_struct.strdl_struct(filename, module_doc, functs)


def get_params(funct_string) -> list:
        functs = []
        for line in funct_string.split('\n'):
            line.strip()
            if 'param' in line:
                split = line.split(' ')
                docs = ''
                for i in range(6, len(split)):
                    docs += split[i] + ' '
                functs.append(strdl_struct.strdl_param(split[0].strip(':'), docs))
        return functs


def get_desc(funct_string) -> str:
    desc = ''
    for line in funct_string.split('\n'):
        if 'param' in line or 'return' in line:
            return desc
        desc += line
    return desc


def get_return(funct_string) -> str:
    ret = ''
    for line in funct_string.split('\n'):
        if 'return:' in line:
            ret += line.strip('return:')
    return ret
