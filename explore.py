import re
import unicodedata
import pandas as pd
import nltk

def show_counts_and_ratios(df, column):
    """
    Takes in a dataframe and a string of a single column
    Returns a dataframe with absolute value counts and percentage value counts
    """
    labels = pd.concat([df[column].value_counts(),
                    df[column].value_counts(normalize=True)], axis=1)
    labels.columns = ['n', 'percent']
    labels
    return labels

def vector_counts(vector_df):
    '''
        Takes in a vectorized dataframe and returns a df with a vectors column 
        and the number of occurrances for each vector 
    '''
    count_dict = {'Vector': [], 'Count': []}
    for col in vector_df.columns:
        count = vector_df[col].values.sum()
        count_dict['Vector'].append(col)
        count_dict['Count'].append(count)
    count_df = pd.DataFrame.from_dict(count_dict, orient = 'columns')
    return count_df.sort_values(by = ['Count'], ascending = False)
