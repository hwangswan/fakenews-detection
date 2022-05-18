"""This module clean data"""

import sys
import pandas as pd

__RANDOM_STATE__ = 42

__TRUE_CSV__ = 'dataset/True.csv'
__FAKE_CSV__ = 'dataset/Fake.csv'
__TRAIN_CSV__ = 'dataset/train.csv'
__TEST_CSV__ = 'dataset/test.csv'

def clean() -> None:
    """Clean data function

    Input:
        - None
    Output:
        - None
    """
    try:
        fake_df = pd.read_csv(__FAKE_CSV__)
        true_df = pd.read_csv(__TRUE_CSV__)
    except FileNotFoundError:
        print('Original Dataset not found.')
        sys.exit(2)

    # Add labels
    fake_df['class'] = 0
    true_df['class'] = 1

    # Create train and test dataset
    fake_df_test = fake_df.tail(50)
    true_df_test = true_df.tail(50)

    fake_df.drop(fake_df.tail(50).index, inplace = True)
    true_df.drop(true_df.tail(50).index, inplace = True)

    train_df = pd.concat([true_df, fake_df], axis = 0)
    test_df = pd.concat([true_df_test, fake_df_test], axis = 0)

    train_df = train_df.drop(['title', 'subject', 'date'], axis = 1)
    test_df = test_df.drop(['title', 'subject', 'date'], axis = 1)

    # Data shuffle
    train_df = train_df.sample(frac = 1, random_state = __RANDOM_STATE__).reset_index(drop = True)
    test_df = test_df.sample(frac = 1, random_state = __RANDOM_STATE__).reset_index(drop = True)

    # Save to csv
    train_df.to_csv(__TRAIN_CSV__)
    test_df.to_csv(__TEST_CSV__)

    print('Successfully saved train_df to', __TRAIN_CSV__, 'test_df to', __TEST_CSV__)

if __name__ == '__main__':
    clean()
