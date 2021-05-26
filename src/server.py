from flask import Flask, request, render_template
import pandas as pd
from prolog_facade import PrologFacade

class Server:
    def __init__(self, host, port):
        self.__app = Flask(__name__, template_folder='../public')
        self.__host = host
        self.__port = port
        self.__prolog = PrologFacade()

    def __load_prolog(self, csv_file):
        data = pd.read_csv(csv_file)

        self.__prolog.consult("./src/analyze.pl")

        for row in data.itertuples():
            self.__prolog.assertz(
                f"game({row.contest}, {row.number_01}, {row.number_02}, {row.number_03}, {row.number_04}, {row.number_05}, {row.number_06})")

    def __register_routers(self):
        self.__app.add_url_rule("/", "index", self.__index)
        self.__app.add_url_rule("/number-drawn", "number_drawn", self.__number_drawn,  methods=['POST'])

    def __index(self):
        return render_template('index.html')

    def __number_drawn(self):
        body = request.get_json()

        if "number" not in body:
            return { 
                "data": {
                    "number": ["Number is required"] 
                }
            }

        drawn = self.__prolog.query("number_drawn({})".format(body['number']))

        return {
            "data": {
                "drawn": True if drawn else False
            }
        }

    def run(self, csv_file):
        self.__load_prolog(csv_file)
        self.__register_routers()
        self.__app.run(host=self.__host, port=self.__port, debug=True)
