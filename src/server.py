from flask import Flask
import pandas as pd
from prolog_facade import PrologFacade

class Server:
    def __init__(self, host, port):
        self.__app = Flask(__name__)
        self.__host = host
        self.__port = port
        self.__prolog = None

    def __load_prolog(self, csv_file):
        data = pd.read_csv(csv_file)

        self.__prolog = PrologFacade()
        self.__prolog.consult("./src/analyze.pl")

        for row in data.itertuples():
            self.__prolog.assertz(f"game({row.contest}, {row.number_01}, {row.number_02}, {row.number_03}, {row.number_04}, {row.number_05}, {row.number_06})")

    def __register_routers(self):
        self.__app.add_url_rule("/", "index", self.__index)

    def __index(self):
        return self.__prolog.query("test(X)")

    def run(self, csv_file):
        self.__load_prolog(csv_file)
        self.__register_routers()
        self.__app.run(host=self.__host, port=self.__port, debug=True)
