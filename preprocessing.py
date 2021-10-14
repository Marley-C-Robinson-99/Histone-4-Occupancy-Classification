import pandas as pd
import numpy as np
import os
import re
from acquire import get_H4_data
from Bio import SeqIO
from Bio.Seq import Seq
from sklearn.model_selection import train_test_split

###################################         SPLITTING        ###################################

def tvt_split(df, y = None):
    '''
    This function takes in a dataframe and, optionally, a target_var array and performs a train, validate, 
    test split with no stratification, make sure to separate target var
    Returns train, validate, and test dfs.
    '''

    if y is None:
        train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=1312)
        train, validate = train_test_split(train_validate, test_size=.3, 
                                    random_state=1312)
        return train, validate, test
    else:
        X_train_validate, X_test, y_train_validate, y_test = train_test_split(df, y,
                                                                        test_size=.2, 
                                                                        random_state=1312)
        X_train, X_validate, y_train, y_validate = train_test_split(X_train_validate, y_train_validate,
                                                                        test_size=.3, 
                                                                        random_state=1312)
        return X_train, X_validate, X_test, y_train, y_validate, y_test
###################################         PREPROCESSING        ###################################
def check_len(df, seq_col = 'sequence', length = 500):
    '''
        Checks the lengths of sequences in a dataframe given the sequence column name
        and compares the lengths to the length defined in the function parameters
    '''
    # Checking for equal length of sequences and assign index to list
    diff_len = []
    for i, seq in enumerate(df[seq_col]):
        if len(seq) == length:
            continue
        if len(seq) != length:
            print(f'Unexpected sequence length at index: {i}, length {len(seq)}.')
            diff_len.append(i)
    
    # Create a dataframe from list using indexes in diff_len
    unexpected = pd.DataFrame(columns = df.columns)
    for i in range(len(diff_len)):
        unexpected = unexpected.append(df[df.index == diff_len[i]])

    return unexpected


def preprocess():
    '''
        This function will clean the data where necessary and attempt to fill any abnormal sequence lengths
        outputs dataframe ready for exploration and modeling
    '''
    # Grabbing data from acquire
    df = get_H4_data()

    # Cleaning id strings with \n appending
    df.id = df.id.apply(lambda x: x.replace('\n', '')) # deleting /n appending each id

def nucleotide_count(df, seq_col = 'sequence'):
    '''
        Creates columns {A: a_count, C: c_count, G: g_count, T: t_count} based on
        the presence of each nucleotide base in the given sequence column for each entry
    '''
    A_count = []
    C_count = []
    T_count = []
    G_count = []
    
    for seq in df[seq_col]:
        A_count.append(Seq(seq).count('A'))
        C_count.append(Seq(seq).count('C'))
        G_count.append(Seq(seq).count('G'))
        T_count.append(Seq(seq).count('T'))
    
    df['adenine'] = A_count
    df['cytosine'] = C_count
    df['guanine'] = G_count
    df['thymine'] = T_count
    
    return df

    
def getKmers(sequence, k=6):
    '''
        Creates KMers of k length given a sequence
    '''
    
    return [sequence[x:x+k].lower() for x in range(len(sequence) - k + 1)]


#df['hexamer'] = df.apply(lambda x: getKmers(x['sequence']), axis=1)
#human_data = human_data.drop('sequence', axis=1)