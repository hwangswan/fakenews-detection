'''This module is the pipeline, clean and predict article'''

import re
import os
import string
import pickle as pkl

class Pipeline:
    '''The pipeline class'''

    def __init__(self) -> None:
        '''Initialise data'''

        self.__model_folder = 'model/'

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

        # Load vectorizer
        if not os.path.exists(self.__model_folder + 'vectorizer.pkl'):
            raise FileNotFoundError('Vectorizer not found: vectorizer.pkl')

        with open(self.__model_folder + 'vectorizer.pkl', 'rb') as file_handler:
            self.__vectorizer = pkl.load(file_handler)

        # Check model existance
        for classifier in self.__classifiers_name:
            if not os.path.exists(self.__model_folder + f'{classifier}.pkl'):
                raise FileNotFoundError(f'Model not found: {classifier}.pkl')

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

        with open(f'{self.__model_folder}{classifier_name}.pkl', 'rb') as file_handler:
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
        return classifier.predict(v_sentences)

    def predict_all(self, sentences : list) -> dict:
        '''Predict a list of sentences with all available classifiers.

        Input:
            - sentences : list of str
        Output
            - Dictionary of keys -> classifier key, value -> predicted labels.
        '''
        result = {}
        for classifier_key in self.__classifiers_name:
            result[classifier_key] = self.predict(classifier_key, sentences)

        return result
