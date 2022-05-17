'''This module train classification models'''

import pickle as pkl
import re
import string
import os
import sys
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

__MODEL_DIR__ = 'model/'
__TRAIN_CSV__ = 'dataset/train.csv'
__TEST_CSV__ = 'dataset/test.csv'

class Train:
    '''This class train models'''

    def __init__(self, random_state = 0) -> None:
        '''Initialise data'''

        if not os.path.exists(__MODEL_DIR__):
            os.makedirs(__MODEL_DIR__)

        self.__random_state = random_state

        x_train, y_train, x_test, y_test = self.__dataloader()
        self.__y_train, self.__y_test = y_train, y_test

        # Create vectorizer
        self.__create_tfidf_vectorizer(x_train, x_test)

    def __dataloader(self) -> tuple:
        '''Load dataset'''

        try:
            df_train = pd.read_csv(__TRAIN_CSV__)
            df_test = pd.read_csv(__TEST_CSV__)
        except FileNotFoundError:
            print('Dataset not found, try running clean.py')
            sys.exit(2)

        # Preprocess data
        df_train['text'].apply(Train.preprocess)
        df_test['text'].apply(Train.preprocess)

        self.__model_dir = __MODEL_DIR__
        x_train, y_train = df_train['text'], df_train['class']
        x_test, y_test = df_test['text'], df_test['class']

        print('Finished reading dataset')

        return x_train, y_train, x_test, y_test

    def __dump(self, variable, filename : str):
        '''Dump a variable to pickle file.
        '''
        with open(self.__model_dir + f'{0}.pkl'.format(filename), 'wb') as file_handler:
            pkl.dump(variable, file_handler)

        print('Finished dumping', filename, end = '\n\n')

    @staticmethod
    def preprocess(text : str) -> str:
        '''This will later be a method inside pipeline.

        Preprocess any string:
            - Lowercase.
            - Removing links.
            - Removing integers.
            - Removing punctutations and endlines.
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

    def __create_tfidf_vectorizer(self, x_train, x_test) -> None:
        '''Create a tfidf vectorizer based on training and testing corpus'''

        self.__vectorizer = TfidfVectorizer(
            stop_words = 'english',
        )

        self.__x_train = self.__vectorizer.fit_transform(x_train)
        self.__x_test = self.__vectorizer.transform(x_test)

        print('TfidfVectorizer params:', self.__vectorizer.get_params())
        print('TfidfVectorizer vocabulary size:', len(self.__vectorizer.vocabulary_))

        self.__dump(self.__vectorizer, 'vectorizer')

    def __train_logistic_regression(self) -> None:
        '''Train logistic regression model'''

        logistic_model = LogisticRegression()

        logistic_model.fit(self.__x_train, self.__y_train)

        model_score = logistic_model.score(self.__x_test, self.__y_test)
        print('Logistic Regression model score:', model_score)

        predicted = logistic_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(logistic_model, 'logistic_regression')

    def __train_sgd(self) -> None:
        '''Train SGDClassifier model'''

        sgd_model = SGDClassifier(random_state = self.__random_state)

        sgd_model.fit(self.__x_train, self.__y_train)

        model_score = sgd_model.score(self.__x_test, self.__y_test)
        print('SGD Classifier model score', model_score)

        predicted = sgd_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(sgd_model, 'sgd_classifier')

    def __train_decision_tree(self) -> None:
        '''Train Decision Tree model'''

        decision_model = DecisionTreeClassifier(
            random_state = self.__random_state,
            criterion = 'entropy'
        )

        decision_model.fit(self.__x_train, self.__y_train)

        model_score = decision_model.score(self.__x_test, self.__y_test)
        print('Decision Tree model score:', model_score)

        predicted = decision_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(decision_model, 'decision_tree')

    def __train_gradient_boosting(self) -> None:
        '''Train Gradient Boosting model'''

        gradient_model = GradientBoostingClassifier(random_state = self.__random_state)

        gradient_model.fit(self.__x_train, self.__y_train)

        model_score = gradient_model.score(self.__x_test, self.__y_test)
        print('Gradient Boosting score:', model_score)

        predicted = gradient_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(gradient_model, 'gradient_boosting')

    def __train_random_forest(self) -> None:
        '''Train Random Forest model'''

        forest_model = RandomForestClassifier(
            random_state = self.__random_state,
            criterion = 'entropy'
        )

        forest_model.fit(self.__x_train, self.__y_train)

        model_score = forest_model.score(self.__x_test, self.__y_test)
        print('Random Forest Classifier model score', model_score)

        predicted = forest_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(forest_model, 'random_forest')

    def __train_k_nearest_neighbors(self) -> None:
        '''Train k-nearest Neighbors model'''

        neighbors_model = KNeighborsClassifier(n_neighbors = 1, weights = 'distance')

        neighbors_model.fit(self.__x_train, self.__y_train)

        model_score = neighbors_model.score(self.__x_test, self.__y_test)
        print('K-Nearest Neighbors model score:', model_score)

        predicted = neighbors_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(neighbors_model, 'k_neighbors')

    def __train_multinomial_naive_bayes(self) -> None:
        '''Train MultinomialNB model'''

        multinomial_bayes_model = MultinomialNB()

        multinomial_bayes_model.fit(self.__x_train, self.__y_train)

        model_score = multinomial_bayes_model.score(self.__x_train, self.__y_train)
        print('Multinomial Bayes model score:', model_score)

        predicted = multinomial_bayes_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(multinomial_bayes_model, 'naive_bayes')

    def __train_linear_svc(self) -> None:
        '''Train Linear Support Vector Classifier model'''

        linear_svc_model = LinearSVC(random_state = self.__random_state)

        linear_svc_model.fit(self.__x_train, self.__y_train)

        model_score = linear_svc_model.score(self.__x_test, self.__y_test)
        print('Linear SVC model score:', model_score)

        predicted = linear_svc_model.predict(self.__x_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(linear_svc_model, 'linear_svc')

    def train(self) -> None:
        '''Train all models'''

        self.__train_logistic_regression()
        self.__train_sgd()
        self.__train_decision_tree()
        self.__train_gradient_boosting()
        self.__train_random_forest()
        self.__train_k_nearest_neighbors()
        self.__train_multinomial_naive_bayes()
        self.__train_linear_svc()

if __name__ == '__main__':
    train = Train(random_state = 42)
    train.train()
