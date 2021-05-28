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

        drawn = self.__prolog.query("number_drawn({})".format(body['number']))

        return {
            "data": {
                "drawn": True if drawn else False
            }
        }
