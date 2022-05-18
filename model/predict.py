"""This module predict an article, giving an input file"""

import getopt
import sys
from pipeline import Pipeline

def main(argv : list) -> None:
    """Main function

    Input:
        - argv: arguments array
    Output:
        - None
    """
    input_file, classifier = '', ''
    all_classifier = False

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'all', 'classifier='])

        for opt, arg in opts:
            if opt == '--input':
                input_file = arg
            if opt == '--all':
                all_classifier = True
            if opt == '--classifier':
                classifier = arg

    except getopt.GetoptError:
        print('Invalid arguments, try again.')
        sys.exit(2)

    if input_file == '':
        print('No input file specified.')
        sys.exit(2)
    if classifier == '' and not all_classifier:
        print('No classifier specified.')
        sys.exit(2)

    try:
        pipeline = Pipeline()

        with open(input_file, 'r+', encoding='utf8') as file_handler:
            article = file_handler.read()

            if not all_classifier:
                print(pipeline.predict(classifier, [article]))
            else:
                print(pipeline.predict_all([article]))
    except AssertionError:
        print('Classifier not found:', classifier)
    except FileNotFoundError as file_error:
        print(str(file_error))

if __name__ == '__main__':
    main(sys.argv[1:])
