from flask import request
from helpers import PrologFacade


class Controllers:
    def __init__(self):
        self.__prolog = PrologFacade()

    """
    Return if number has ever been drawn.

    Body (JSON):
        "number": int 1 > number <= 60

    Returns:
        bool: True for drawn, False not drawn.
    """

    def number_drawn(self):
        body = request.get_json()
        if not body:
            return {"error": "Wrong format"}, 422

        if "number" not in body:
            return {
                "error": {
                    "number": ["Number is required"]
                }
            }, 400

        drawn = self.__prolog.query("number_drawn({})".format(body["number"]))

        return {
            "data": {
                "drawn": True if drawn else False
            }
        }

    def winning_game(self):
        body = request.get_json()
        if not body:
            return {"error": "Wrong format"}, 422

        # TODO: Melhorar a validação
        if "game" not in body:
            return {
                "error": {
                    "game": ["Game is required"]
                }
            }, 400

        winning = self.__prolog.query("winning_game({}, {}, {}, {}, {}, {})".format(
            body["game"]["n1"],
            body["game"]["n2"],
            body["game"]["n3"],
            body["game"]["n4"],
            body["game"]["n5"],
            body["game"]["n6"]
        ))

        return {
            "data": {
                "win": True if winning else False
            }
        }

    def never_drawn(self):
        return {
            "data": {
                "ok": True
            }
        }

    def win_the_game_more_often(self):
        return {
            "data": {
                "ok": True
            }
        }

    def number_drawn_how_many_times(self):
        return {
            "data": {
                "ok": True
            }
        }

    def more_drawn_number(self):
        return {
            "data": {
                "ok": True
            }
        }
