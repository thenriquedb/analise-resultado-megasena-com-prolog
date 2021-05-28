from flask import Flask, render_template
from controllers import Controllers


class Server:
    def __init__(self, host, port):
        self.__app = Flask(__name__, template_folder='./templates')
        self.__app.config.update(
            TESTING=True,
            TEMPLATES_AUTO_RELOAD=True
        )
        self.__host = host
        self.__port = port
        self.__controllers = Controllers()

    def __register_routers(self):
        self.__app.add_url_rule("/", "index", self.__index)
        self.__app.add_url_rule(
            "/number-drawn", "number_drawn", self.__number_drawn, methods=['POST'])

    def __index(self):
        return render_template('index.jinja-html')

    def __number_drawn(self):
        return self.__controllers.number_drawn()

    def run(self):
        self.__register_routers()
        self.__app.run(host=self.__host, port=self.__port, debug=True)
