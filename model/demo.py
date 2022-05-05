from pipeline import Pipeline
import getopt, sys

def main(argv):
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
        p = Pipeline()

        with open(input_file, 'r+') as f:
            if not all_classifier:
                print(p.predict(classifier, f.readlines()))
            else:
                print(p.predict_all(f.readlines()))
    except AssertionError:
        print('Classifier not found:', classifier)

if __name__ == '__main__':
    main(sys.argv[1:])