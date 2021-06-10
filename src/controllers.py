from flask import request
from helpers import PrologFacade
from http import HTTPStatus

STATUS_CODE = 200


class Controllers:
    def __init__(self):
        self.__prolog = PrologFacade()

    def __body_validation(self, body: dict, fields: list):
        if not body:
            return {"error": "Wrong format"}, HTTPStatus.ACCEPTED

        fields_dict = {}
        for field in fields:
            fields_dict[field] = False

        for key in body.keys():
            if not fields_dict[key]:
                field[key] = True

        response = {"error": {}}
        status_code = HTTPStatus.ACCEPTED
        for field in fields_dict:
            if not fields_dict[key]:
                response["error"][key] = '{} is required'.format(key)
                status_code = HTTPStatus.UNPROCESSABLE_ENTITY

        return response, status_code

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
            return {"error": "Wrong format"}, 422
        # __body_validation
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

    def check_occurence_of_drawn_number(self):
        body = request.get_json()
        if not body:
            return {"error": "Wrong format"}, 422

        query = "count_occ({}, Count)".format(body["number"])
        result = self.__prolog.query(query)

        return {
            "data": {
                "count": result[0]['Count']
            }
        }

    def more_drawn_number(self):
        return {
            "data": {
                "ok": True
            }
        }
