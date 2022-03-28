from pipeline import Pipeline
import getopt, sys

def main(argv):
    input_file, classifier = '', ''

    try:
        opts, _ = getopt.getopt(argv, 'hi:o', ['input=', 'classifier='])

        for opt, arg in opts:
            if opt == '--input':
                input_file = arg
            if opt == '--classifier':
                classifier = arg

    except getopt.GetoptError:
        print('Invalid arguments, try again.')
        sys.exit(2)

    if input_file == '':
        print('No input file specified.')
        sys.exit(2)
    if classifier == '':
        print('No classifier specified.')
        sys.exit(2)

    p = Pipeline()

    # Demo sentence prediction with SGDClassifier
    p.set_classifier(classifier)

    with open(input_file, 'r+') as f:
        print(p.predict(f.readlines()))

if __name__ == '__main__':
    main(sys.argv[1:])