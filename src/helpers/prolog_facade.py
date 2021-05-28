from .prolog_MT import PrologMT


class PrologFacade:
    def __init__(self):
        self.__prolog = PrologMT()

    def consult(self, path: str):
        self.__prolog.consult(path)

    def query(self, query: list):
        return list(self.__prolog.query(query))

    def assertz(self, fact: str):
        return self.__prolog.assertz(fact)

    def unify(self, fact1, fact2):
        return fact1 == fact2
