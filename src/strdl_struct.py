class strdl_struct:

    __slots__ = {"filename", "file_docs", "methods"}

    def strdl_struct(self, filename, file_docs, methods):
        self.filename = filename
        self.file_docs = file_docs
        self.methods = methods


class strdl_method:

    __slots__ = {"name", "params"}

    def strudl_method(self, name, params):
        self.name = name
        self.params = params

    def pretty_params(self) -> str:
        pretty = ''
        for param in self.params:
            pretty += str(param.param) + ': ' + str(param.docs) + '\n'
        return pretty


class strdl_param:

    __slots__ = {"param", "docs"}

    def strdl_param(self, param, docs):
        self.param = param
        self.docs = docs