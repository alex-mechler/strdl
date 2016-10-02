class strdl_struct:

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

    __slots__ = {"name", "params"}

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def __str__(self):
        return self.name + ': ' + self.params

    def pretty_params(self) -> str:
        pretty = ''
        for param in self.params:
            pretty += str(param) + '\n'
        return pretty


class strdl_param:

    __slots__ = {"param", "docs"}

    def __init__(self, param, docs):
        self.param = param
        self.docs = docs

    def __str__(self):
        return self.param + ': ' + self.docs
