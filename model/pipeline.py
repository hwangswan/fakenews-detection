import pickle as pkl
import re, string

class Pipeline:
    def __init__(self):
        self.__classifiers_name = [
            'logistic_regression',
            'sgd_classifier',
            'decision_tree',
            'gradient_boosting',
            'random_forest',
            'k_neighbors',
            'naive_bayes',
            'linear_svc'
        ]

        with open('vectorizer.pkl', 'rb') as f:
            self.__vectorizer = pkl.load(f)
    
    def set_classifier(self, classifier_name):
        assert classifier_name in self.__classifiers_name

        with open('{0}.pkl'.format(classifier_name), 'rb') as f:
            self.__classifier = pkl.load(f)

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

    def predict(self, sentences : list) -> list:
        '''Predict a list of sentences.

        Input:
            - sentences : list of str
        Output:
            - list
        '''
        sentences = [Pipeline.preprocess(s) for s in sentences]
        v_sentences = self.__vectorizer.transform(sentences)
        return self.__classifier.predict(v_sentences)