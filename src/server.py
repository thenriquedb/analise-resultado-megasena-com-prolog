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
            "/number-drawn",
            "number_drawn",
            self.__number_drawn,
            methods=['POST'])

        self.__app.add_url_rule(
            "/winning-game",
            "winning_game",
            self.__winning_game,
            methods=['POST'])

        self.__app.add_url_rule(
            "/never-drawn",
            "never_drawn",
            self.__never_drawn,
            methods=['POST'])

        self.__app.add_url_rule(
            "/win-the-game-more-often",
            "win_the_game_more_often",
            self.__win_the_game_more_often,
            methods=['POST'])

        self.__app.add_url_rule(
            "/number-drawn-how-many-times",
            "number_drawn_how_many_times",
            self.__check_occurence_of_drawn_number,
            methods=['POST'])

        self.__app.add_url_rule(
            "/more-drawn-number",
            "more_drawn_number",
            self.__more_drawn_number,
            methods=['POST'])

    def __index(self):
        return render_template('index.jinja-html')

    def __number_drawn(self):
        return self.__controllers.number_drawn()

    def __winning_game(self):
        return self.__controllers.winning_game()

    def __never_drawn(self):
        return self.__controllers.never_drawn()

    def __win_the_game_more_often(self):
        return self.__controllers.win_the_game_more_often()

    def __check_occurence_of_drawn_number(self):
        return self.__controllers.check_occurence_of_drawn_number()

    def __more_drawn_number(self):
        return self.__controllers.more_drawn_number()

    def run(self):
        self.__register_routers()
        self.__app.run(host=self.__host, port=self.__port, debug=True)
