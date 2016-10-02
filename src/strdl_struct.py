"""
strdl is a HTML documentation generator for python file

strdl_struct.py is a collection of classes that store the structure for a strdl documentation

author: Alexander Mechler

Copyright (C) 2016 Alexander Mechler

Licenced under the MIT license
"""


class strdl_struct:
    """
    A class representing a full file.
    """

    __slots__ = {"filename", "file_docs", "functs"}

    def __init__(self, filename, file_docs, functs):
        self.filename = filename
        self.file_docs = file_docs
        self.functs = functs

    def __str__(self):
        pretty = self.filename + '\n' + self.file_docs + '\n'
        for funct in self.functs:
            pretty += funct.name + ':\n' + funct.pretty_params() + '\n'
        return pretty


class strdl_method:
    """
    A class representing an individual method
    """

    __slots__ = {'name', 'desc', 'params', 'return_doc'}

    def __init__(self, name, desc, params, return_doc):
        self.name = name
        self.desc = desc
        self.params = params
        self.return_doc = return_doc

    def __str__(self):
        return self.name + ': ' + self.desc + '\n' + self.params + '\n' + self.return_doc

    def pretty_params(self) -> str:
        pretty = ''
        for param in self.params:
            pretty += str(param) + '\n'
        return pretty


class strdl_param:
    """
    A class storing a single parameter of a method
    """

    __slots__ = {"param", "docs"}

    def __init__(self, param, docs):
        self.param = param
        self.docs = docs

    def __str__(self):
        return self.param + ': ' + self.docs
