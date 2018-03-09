#!/usr/bin/python
#matplotlib inline

from IPython.display import Image
import matplotlib as mlp
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sklearn

from sklearn import cross_validation
from sklearn import tree
from sklearn import svm
from sklearn import ensemble
from sklearn import neighbors
from sklearn import linear_model
from sklearn import metrics
from sklearn import preprocessing

plt.style.use('fivethirtyeight') # Good looking plots
pd.set_option('display.max_columns', None) # Display any number of columns

_DATA_DIR = os.getcwd()
_CHURN_DATA_PATH = os.path.join(_DATA_DIR, 'Workbook1.csv')

import seaborn as sns

df = pd.read_csv(_CHURN_DATA_PATH)
df.head()

# Discreet value integer encoder
label_encoder = preprocessing.LabelEncoder()

# Get the Labels as integers
y = df['label'].as_matrix().astype(np.int)
df.drop(['label'], axis=1, inplace=True)

print('There are {} instances for churn class and {} instances for not-churn classes.'.format(y.sum(), y.shape[0] - y.sum()))
X = df.as_matrix().astype(np.float)
scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)


def stratified_cv(X, y, clf_class, shuffle=True, n_folds=10, **kwargs):
    stratified_k_fold = cross_validation.StratifiedKFold(y, n_folds=n_folds, shuffle=shuffle)
    y_pred = y.copy()
    for ii, jj in stratified_k_fold:
        X_train, X_test = X[ii], X[jj]
        y_train = y[ii]
        clf = clf_class(**kwargs)
        clf.fit(X_train,y_train)
        y_pred[jj] = clf.predict(X_test)
    return y_pred


print('Linear Regression:\n {}\n'.format(metrics.classification_report(y, stratified_cv(X, y, linear_model.LinearRegression))))
print('Decision Tree Classifier:\n {}\n'.format(metrics.classification_report(y, stratified_cv(X, y, tree.DecisionTreeClassifier))))
print('Support vector machine(SVM):\n {}\n'.format(metrics.classification_report(y, stratified_cv(X, y, svm.SVC))))
print('Random Forest Classifier:\n {}\n'.format(metrics.classification_report(y, stratified_cv(X, y, ensemble.RandomForestClassifier))))
print('Logistic Regression:\n {}\n'.format(metrics.classification_report(y, stratified_cv(X, y, linear_model.LogisticRegression))))