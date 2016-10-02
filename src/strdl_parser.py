"""
strdl is a HTML documentation generator for python file

strdl_parser.py parses in an individual file and stores it in a strudl_struct

author: Alexander Mechler

Copyright (C) 2016 Alexander Mechler

Licenced under the MIT license
"""

import inspect
import importlib
import strdl_struct


def parse(file):
    """
    Main parsing function
    :param file: The python file to parse
    :return: A strdl_struct with all relevant information
    """
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
    """
    Parses the parameters from a particular function
    :param funct_string: The documentation to pull the parameters from
    :return: A list of all parameters for the passed documentation
    """
    functs = []
    for line in funct_string.split('\n'):
        line.strip()
        if 'param' in line:
            split = line.split(' ')
            docs = ''
            for i in range(5, len(split)):
                docs += split[i] + ' '
                functs.append(strdl_struct.strdl_param(split[4].strip(':').strip(), docs))
    return functs


def get_desc(funct_string) -> str:
    """
    Get the description of the function
    :param funct_string: The documentation to pull the description from
    :return: A string of the description
    """
    desc = ''
    for line in funct_string.split('\n'):
        if 'param' in line or 'return' in line:
            return desc
        desc += line
    return desc


def get_return(funct_string) -> str:
    """
    Get the return documentation for a function
    :param funct_string: The documentation to pull the return from
    :return: A string of the return documentation
    """
    ret = ''
    for line in funct_string.split('\n'):
        if 'return:' in line:
            split = line.split();
            if len(split) > 1:
                for i in range(1, len(split)):
                    ret += split[i] + ' '
    return ret
