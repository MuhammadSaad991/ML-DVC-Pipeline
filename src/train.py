import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from catboost import CatBoostClassifier
from sklearn import svm
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report
from sklearn.model_selection import cross_val_score
import json
import pickle
import os
import dvc.api

#  storage URL and file path

file_path = 'data/data_preprocessed.csv'

RFC_METRIC = 'gini'  #metric used for RandomForrestClassifier
NUM_ESTIMATORS = 100 #number of estimators used for RandomForrestClassifier
NO_JOBS = 4 #number of parallel jobs used for RandomForrestClassifier
#TRAIN/VALIDATION/TEST SPLIT
#VALIDATION
VALID_SIZE = 0.20 # simple validation using train_test_split
TEST_SIZE = 0.20 # test size using_train_test_split
#CROSS-VALIDATION
NUMBER_KFOLDS = 5 #number of KFolds for cross-validation
RANDOM_STATE = 42
MAX_ROUNDS = 1000 #lgb iterations
EARLY_STOP = 50 #lgb early stop 
OPT_ROUNDS = 1000  #To be adjusted based on best validation rounds
VERBOSE_EVAL = 50 #Print out metric result





if os.path.isfile("data/creditcard.csv"):
    print("Train file Data access locally")
    df = pd.read_csv('./data/data_preprocessed.csv')
else:
    print("Train file Data access locally")
    with dvc.api.open(url=file_path,remote='storage',mode='r',repo='.') as fd:
        df = pd.read_csv(fd)




target = 'Class'
predictors = ['scaled_time', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',\
       'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19',\
       'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28',\
       'scaled_amount']


train_df, test_df = train_test_split(df, test_size=TEST_SIZE, random_state=RANDOM_STATE, shuffle=True )
train_df, valid_df = train_test_split(train_df, test_size=VALID_SIZE, random_state=RANDOM_STATE, shuffle=True )

clf = RandomForestClassifier(n_jobs=NO_JOBS, 
                             random_state=RANDOM_STATE,
                             criterion=RFC_METRIC,
                             n_estimators=NUM_ESTIMATORS,
                             verbose=False)


clf.fit(train_df[predictors], train_df[target].values)

preds = clf.predict(valid_df[predictors])

acc = roc_auc_score(valid_df[target].values, preds)

training_score = cross_val_score(clf, train_df[predictors], train_df[target].values, cv=5)

print("Accuracy =",acc)
print("Train Accuracy =",training_score)

with open("metrics.json", 'w') as outfile:
        json.dump({ "accuracy": acc, "training_score": training_score[0]}, outfile)


# Save the model to a file using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)