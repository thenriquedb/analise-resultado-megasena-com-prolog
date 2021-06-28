from flask import request
from helpers import PrologFacade
from http import HTTPStatus


class Controllers:
    def __init__(self):
        self.__prolog = PrologFacade()

    def number_drawn(self):
        """
        Return if number has ever been drawn.

        Body (JSON):
            "number": int 1 > number <= 60

        Returns:
            bool: True for drawn, False not drawn.
        """
        body = request.get_json()
        # self.__body_validation(self, body, ['number'])
        if not body:
            return {"error": "Wrong format"}, HTTPStatus.UNPROCESSABLE_ENTITY
        # __body_validation
        if "number" not in body:
            return {
                "error": {
                    "number": ["Number is required"]
                }
            }, HTTPStatus.BAD_REQUEST

        drawn = self.__prolog.query("number_drawn({})".format(body["number"]))

        return {
            "data": {
                "drawn": True if drawn else False
            }
        }

    def winning_game(self):
        body = request.get_json()
        if not body:
            return {"error": "Wrong format"}, HTTPStatus.UNPROCESSABLE_ENTITY

        # TODO: Melhorar a validação
        if "game" not in body:
            return {
                "error": {
                    "game": ["Game is required"]
                }
            }, HTTPStatus.BAD_REQUEST

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
        result = self.__prolog.query("never_drawn(List)")
        return {
            "data": {
                "list": result[0]["List"]
            }
        }

    def win_the_game_more_often(self):
        results = self.__prolog.query("more_drawn_game(X)")
        # Remove duplicate items
        results_set = set()
        for result in results:
            result_tuple_a = tuple(result["X"])
            results_set.add(result_tuple_a)

        return {
            "data": {
                "list": list(results_set),
            }
        }

    def check_occurence_of_drawn_number(self):
        body = request.get_json()
        if not body:
            return {"error": "Wrong format"}, HTTPStatus.UNPROCESSABLE_ENTITY

        query = "count_occ({}, Count)".format(body["number"])
        result = self.__prolog.query(query)

        return {
            "data": {
                "count": result[0]['Count']
            }
        }

    def more_drawn_number(self):
        query = "more_drawn_number(L)"
        result = self.__prolog.query(query)

        return {
            "data": {
                "number": result[0]['L']
            }
        }
