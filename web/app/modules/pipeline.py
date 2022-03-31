from flask import current_app

import pickle as pkl
import re, string

import os

class Pipeline:
    def __init__(self):
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

        vectorizer_path = os.path.join(current_app.root_path, self.__model_folder, 'vectorizer.pkl')

        with open(vectorizer_path, 'rb') as f:
            self.__vectorizer = pkl.load(f)

    def __load_classifier(self, classifier_name : str):
        '''Load a classifier from pickle file.

        Input:
            - classifier_name : str
        Output:
            - Classifier object
        '''
        assert classifier_name in self.__classifiers_name.keys()

        classifier_path = os.path.join(current_app.root_path, self.__model_folder, '{0}.pkl'.format(classifier_name))

        with open(classifier_path, 'rb') as f:
            classifier = pkl.load(f)
        
        return classifier
    
    def get_classifiers_list(self) -> list:
        '''Get classifiers list.'''
        return self.__classifiers_name

    @staticmethod
    def preprocess(text : str) -> str:
        '''Preprocessing the text

        Input:
            - text : str
        
        Output:
            - str
        '''
        punctuations = '[{0}]'.format(string.punctuation)

        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('\\W', ' ', text)
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub(punctuations, '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        
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
        for classifier_key in self.__classifiers_name.keys():
            result[classifier_key] = self.predict(classifier_key, sentences)[0]
        
        return result
