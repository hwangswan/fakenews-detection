from flask import request

class Utils:
    @staticmethod
    def get_input(input_name : str) -> str:
        input_val = request.form[input_name]

        if input_val is None or len(input_val) == 0:
            raise Exception('Missing ' + input_name)
        else:
            return input_val
