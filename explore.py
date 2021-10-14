import re
import unicodedata
import pandas as pd
import nltk
from scipy import stats

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

def co_linearity(df, target, cat_vars):
    '''returns a df of all p values and chi2
    scores based on the specified categorical variables and target'''
    cat = cat_vars.copy()
    cat.remove(target)
    
    chi2s = []
    p_score = []
    pdf = pd.DataFrame(columns = ['feature', 'p_values', 'chi2'])
    pdf['feature'] = list(cat)
    
    for i, var in enumerate(cat):
        observed = pd.crosstab(df[cat_vars[i]], df[target])
        chi2, p, degf, expected = stats.chi2_contingency(observed)
        p_score.append(p)
        chi2s.append(chi2)
    
    pdf['p_values'] = p_score
    pdf['chi2'] = chi2s
    pdf = pdf.sort_values(['p_values'], ascending = [True])
    return pdf.reset_index(drop = True)

def pearsons(df, target, quant_vars):
    '''Preforms pearsons r tests on each quant_var against target'''
    quant = quant_vars.copy()
    quant.remove(target)

    corrs = []
    p_score = []
    pdf = pd.DataFrame(columns = ['feature', 'p_values', 'corr'])
    pdf['feature'] = list(quant)
    
    for var in quant:
        corr, p = stats.pearsonr(df[target], df[var])
        p_score.append(p)
        corrs.append(corr)
    
    pdf['p_values'] = p_score
    pdf['corr'] = corrs
    pdf = pdf.sort_values(['p_values'], ascending = [True])
    return pdf.reset_index(drop = True)