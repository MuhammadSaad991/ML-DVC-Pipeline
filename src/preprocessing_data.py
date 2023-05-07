import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler, RobustScaler
import os
import dvc.api


# DVC storage remote and file path
remote = 'storage'
file_path = 'data/creditcard.csv'


# RobustScaler 
std_scaler = StandardScaler()
rob_scaler = RobustScaler()


if os.path.isfile("data/creditcard.csv"):
    df = pd.read_csv('./data/creditcard.csv')
else:
    with dvc.api.open(path=file_path, mode='r', remote=remote, repo='.') as fd:
        df = pd.read_csv(fd)

# The classes are heavily skewed we need to solve this issue later.
print('No Frauds', round(df['Class'].value_counts()[0]/len(df) * 100,2), '% of the dataset')
print('Frauds', round(df['Class'].value_counts()[1]/len(df) * 100,2), '% of the dataset')

df['scaled_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
df['scaled_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))

df.drop(['Time','Amount'], axis=1, inplace=True)

scaled_amount = df['scaled_amount']
scaled_time = df['scaled_time']

df.drop(['scaled_amount', 'scaled_time'], axis=1, inplace=True)
df.insert(0, 'scaled_amount', scaled_amount)
df.insert(1, 'scaled_time', scaled_time)

df.to_csv("./data/data_preprocessed.csv")
