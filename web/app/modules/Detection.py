from flask_restful import Resource
from .Utils import Utils

# Import pipeline here

class Detection(Resource):
    def post(self):
        try:
            article_content = Utils.get_input('article_content')

            # And using it here.

            return {
                'error' : False,
                'article_content' : article_content
            }, 200
        except Exception as e:
            return {
                'error' : True,
                'message' : str(e)
            }, 400

