import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.gaussian_process.kernels import RBF
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import KFold, cross_val_score, cross_validate
import warnings
warnings.simplefilter('ignore')

def classifier_models(X_data, y_data, classifier_names, classifier_models):
    '''
        Takes two arrays:
        - X_data = data without the target_var included
        - y_data = an array of the target_var
        - List of model names 
        - List of the classifiers themselves
        
        Preforms cross-validation and returns a metrics dataframe with the model name and accuracy score. 
    '''
    # Zipping models and Classifiers
    models = zip(classifier_names, classifier_models)

    # Cross-validating accuracy for each model based on Train subset
    names = []
    result = []
    coeff = []
    for i, (name, model) in enumerate(models):
        kfold = KFold(n_splits = 10)
        scores = cross_validate(model, X_data, y_data, cv = kfold, scoring = 'accuracy', return_estimator=True)
        result.append(scores)
        names.append(name)
        try:
            coeff.append(model.coeff_)
        except AttributeError:
            coeff.append(None)
        msg = "{0}: Accuracy: {1}, Coeff: {2}".format(name, scores['test_score'].mean(), coeff[i])
        print(msg)
        
    results = [res['test_score'].mean() for res in result]
    metrics_df = pd.DataFrame(data = zip(names, results), columns = ['Model', 'Accuracy'])
    return metrics_df.sort_values(by = ['Accuracy'], ascending = False)