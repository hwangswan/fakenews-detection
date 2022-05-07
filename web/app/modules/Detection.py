from flask_restful import Resource

from .Utils import Utils
from .pipeline import Pipeline

class Detection(Resource):
    def __init__(self):
        self.__p = Pipeline()
    
    def post(self):
        try:
            article_content = Utils.get_input('article_content')
            classifiers_list = self.__p.get_classifiers_list()

            return {
                'error' : False,
                'result' : self.__p.predict_all([article_content]),
                'total_classifiers' : len(classifiers_list)
            }, 200
        except Exception as e:
            return {
                'error' : True,
                'message' : str(e)
            }, 400
