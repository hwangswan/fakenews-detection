'''This module is the pipeline, clean and predict article'''

import re
import os
import string
import pickle as pkl

from flask import current_app

class Pipeline:
    '''The pipeline class'''

    def __init__(self) -> None:
        '''Initialise data'''

        self.__model_folder = os.path.join(current_app.root_path, 'model/')

        self.__classifiers_name = {
            'logistic_regression' : 'Logistic Regression',
            'sgd_classifier' : 'SGD Classifier',
            'decision_tree' : 'Decision Tree',
            'gradient_boosting' : 'Gradient Boosting',
            'random_forest' : 'Random Forest Classifier',
            'k_neighbors' : 'K-Nearest Neighbors',
            'naive_bayes' : 'Multinomial Naive Bayes',
            'linear_svc' : 'Linear Support Vector Classifier'
        }

        # Load classifier
        vectorizer_path = os.path.join(self.__model_folder, 'vectorizer.pkl')

        if not os.path.exists(vectorizer_path):
            file_error = FileNotFoundError('Vectorizer not found: vectorizer.pkl')
            raise file_error

        with open(vectorizer_path, 'rb') as file_handler:
            self.__vectorizer = pkl.load(file_handler)

        # Check for model existance
        for classifier in self.__classifiers_name:
            if not os.path.exists(self.__model_folder + f'{classifier}.pkl'):
                file_error = FileNotFoundError(f'Model not found: {classifier}.pkl')
                raise file_error

    def get_classifiers_list(self) -> dict:
        '''Get all classifiers this pipeline supports'''
        return self.__classifiers_name

    def __load_classifier(self, classifier_name : str):
        '''Load a classifier from pickle file.

        Input:
            - classifier_name : str
        Output:
            - Classifier object
        '''
        if classifier_name not in self.__classifiers_name:
            raise AssertionError('Classifier not in known classifiers list')

        classifier_path = os.path.join(self.__model_folder, f'{classifier_name}.pkl')

        with open(classifier_path, 'rb') as file_handler:
            classifier = pkl.load(file_handler)

        return classifier

    @staticmethod
    def preprocess(text : str) -> str:
        '''Preprocessing the text

        Input:
            - text : str

        Output:
            - str
        '''
        punctuations = f'[{string.punctuation}]'

        text = text.lower()
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'\\W', ' ', text)
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        text = re.sub(r'<.*?>+', '', text)
        text = re.sub(punctuations, '', text)
        text = re.sub(r'\n', '', text)
        text = re.sub(r'\w*\d\w*', '', text)

        return text

    def predict(self, classifier : str, sentences : list) -> list:
        '''Predict a list of sentences.

        Input:
            - sentences : list of str
            - classifier : classifier key
        Output:
            - list
        '''
        sentences = [Pipeline.preprocess(s) for s in sentences]
        classifier = self.__load_classifier(classifier)
        v_sentences = self.__vectorizer.transform(sentences)
        return classifier.predict(v_sentences).tolist()

    def predict_all(self, sentences : list) -> dict:
        '''Predict a list of sentences with all available classifiers.

        Input:
            - sentences : list of str
        Output
            - Dictionary of keys -> classifier key, value -> predicted labels.
        '''
        result = {}
        for classifier_key in self.__classifiers_name:
            result[classifier_key] = self.predict(classifier_key, sentences)[0]

        return result
