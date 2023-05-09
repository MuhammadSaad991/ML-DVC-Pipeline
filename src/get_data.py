import zipfile
import subprocess
import pandas as pd
import os
import dvc.api


# DVC storage remote and file path
remote = 'storage'
file_path = 'data/creditcard.csv'

if os.path.isfile(file_path):
    print("Already Data available")
    df = pd.read_csv(file_path)
    print(df.head(3))
    df.to_csv("./data/creditcard.csv")
else:
    subprocess.run(['kaggle', 'datasets', 'download', '-d', 'mlg-ulb/creditcardfraud'])
    with zipfile.ZipFile('./creditcardfraud.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')
    os.remove("creditcardfraud.zip")
    
    # with dvc.api.open(path=file_path, mode='r', remote=remote, repo='.') as fd:
    #     print("Access data gdrive")
    #     df = pd.read_csv(fd)
    #     print(df.head(3))

    #     print("data shape gdrive",df.shape)

    #     df.to_csv("./data/creditcard.csv")

        # if df.empty:
        #     subprocess.run(['kaggle', 'datasets', 'download', '-d', 'mlg-ulb/creditcardfraud'])
            
        #     with zipfile.ZipFile('./creditcardfraud.zip', 'r') as zip_ref:
        #         zip_ref.extractall('./data')
        #     os.remove("creditcardfraud.zip")


        







# git init
# dvc init

# dvc add data.csv
# git add .gitignore data.csv.dvc
# git commit -m "Add data"

# dvc remote add -d storage gdrive://
# git commit .dvc/config -m "Configure remote stroage"

# dvc push



# dvc run -n data -d get_data.py -o creditcard.csv --no-exec python get_data.py

# dvc repro

# visualize pipeline
# dvc dag


# git add dvc.lock 'data\.gitignore' .gitignore
# git commit -m "Add .gitignore file to ignore data folder"

# git push origin main



