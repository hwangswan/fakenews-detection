'''Utility module'''

from flask import request

def get_input(input_name : str) -> str:
    '''Get input from input_name'''

    input_val = request.form[input_name]

    if input_val is None or len(input_val) == 0:
        raise AssertionError(f'Missing {input_name}')

    return input_val
