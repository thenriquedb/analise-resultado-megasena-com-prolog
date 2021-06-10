
from helpers import PrologFacade
from helpers import PrepareFile
from server import Server


class App:
    def __init__(self, host='localhost', port=4000):
        self.__server = None
        self.__prolog = PrologFacade()
        self.__data = None
        self.__host = host
        self.__port = port

    def load_games(self, csv_path: str):
        print(csv_path)
        self.__data = PrepareFile(csv_path)
        self.__prolog.consult("./src/analyze.pl")

        for row in self.__data.itertuples():
            self.__prolog.assertz(
                f"game({row.contest}, {row.number_01}, {row.number_02}, {row.number_03}, {row.number_04}, {row.number_05}, {row.number_06})")

    def start(self):
        self.__server = Server(self.__host, self.__port)
        self.__server.run()
