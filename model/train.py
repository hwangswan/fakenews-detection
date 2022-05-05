from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

import pandas as pd
import pickle as pkl
import re, string, os

__MODEL_DIR__ = 'model/'
__TRAIN_CSV__ = 'dataset/train.csv'
__TEST_CSV__ = 'dataset/test.csv'

class Train:
    def __init__(self, random_state = 0):
        if not os.path.exists(__MODEL_DIR__):
            os.makedirs(__MODEL_DIR__)

        self.__random_state = random_state
    
        try:
            df_train = pd.read_csv(__TRAIN_CSV__)
            df_test = pd.read_csv(__TEST_CSV__)
        except FileNotFoundError:
            print('Dataset not found, try running dataclean.py')

        # Preprocess data    
        df_train['text'].apply(Train.preprocess)
        df_test['text'].apply(Train.preprocess)

        self.__model_dir = __MODEL_DIR__
        X_train, self.__y_train = df_train['text'], df_train['class']
        X_test, self.__y_test = df_test['text'], df_test['class']

        print('Finished reading dataset')

        # Create vectorizer
        self.__vectorizer = TfidfVectorizer(
            stop_words = 'english',
        )

        self.__X_train = self.__vectorizer.fit_transform(X_train)
        self.__X_test = self.__vectorizer.transform(X_test)

        self.__dump(self.__vectorizer, 'vectorizer')
    
    def __dump(self, variable, filename : str):
        '''Dump a variable to pickle file.
        '''
        with open(self.__model_dir + '{0}.pkl'.format(filename), 'wb') as f:
            pkl.dump(variable, f)

        print('Finished dumping', filename)

    @staticmethod
    def preprocess(text : str) -> str:
        '''This will later be a method inside pipeline.

        Preprocess any string:
            - Lowercase.
            - Removing links.
            - Removing integers.
            - Removing punctutations and endlines.
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

    def __train_logistic_regression(self):
        logistic_model = LogisticRegression()
        logistic_model.fit(self.__X_train, self.__y_train)

        print('Logistic Regression model score:', logistic_model.score(self.__X_test, self.__y_test))
        
        predicted = logistic_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(logistic_model, 'logistic_regression')

    def __train_sgd(self):
        sgd_model = SGDClassifier(random_state = self.__random_state)
        sgd_model.fit(self.__X_train, self.__y_train)

        print('SGD Classifier model score', sgd_model.score(self.__X_test, self.__y_test))

        predicted = sgd_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(sgd_model, 'sgd_classifier')

    def __train_decision_tree(self):
        decision_model = DecisionTreeClassifier(
            random_state = self.__random_state,
            criterion = 'entropy'
        )
        decision_model.fit(self.__X_train, self.__y_train)

        print('Decision Tree model score:', decision_model.score(self.__X_test, self.__y_test))

        predicted = decision_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(decision_model, 'decision_tree')

    def __train_gradient_boosting(self):
        gradient_model = GradientBoostingClassifier(random_state = self.__random_state)
        gradient_model.fit(self.__X_train, self.__y_train)

        print('Gradient Boosting score:', gradient_model.score(self.__X_test, self.__y_test))

        predicted = gradient_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(gradient_model, 'gradient_boosting')

    def __train_random_forest(self):
        forest_model = RandomForestClassifier(
            random_state = self.__random_state,
            criterion = 'entropy'
        )
        forest_model.fit(self.__X_train, self.__y_train)

        print('Random Forest Classifier model score', forest_model.score(self.__X_test, self.__y_test))

        predicted = forest_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(forest_model, 'random_forest')
    
    def __train_k_nearest_neighbors(self):
        neighbors_model = KNeighborsClassifier(n_neighbors = 1, weights = 'distance')
        neighbors_model.fit(self.__X_train, self.__y_train)

        print('K-Nearest Neighbors model score:', neighbors_model.score(self.__X_test, self.__y_test))

        predicted = neighbors_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(neighbors_model, 'k_neighbors')

    def __train_multinomial_naive_bayes(self):
        multinomial_bayes_model = MultinomialNB()
        multinomial_bayes_model.fit(self.__X_train, self.__y_train)

        print('Multinomial Bayes model score:', multinomial_bayes_model.score(self.__X_test, self.__y_test))

        predicted = multinomial_bayes_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(multinomial_bayes_model, 'naive_bayes')

    def __train_linear_svc(self):
        linear_svc_model = LinearSVC(random_state = self.__random_state)
        linear_svc_model.fit(self.__X_train, self.__y_train)

        print('Linear SVC model score:', linear_svc_model.score(self.__X_test, self.__y_test))

        predicted = linear_svc_model.predict(self.__X_test)
        print(classification_report(self.__y_test, predicted))

        self.__dump(linear_svc_model, 'linear_svc')

    def train(self):
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