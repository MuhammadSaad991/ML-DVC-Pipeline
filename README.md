# Credit Card Fraud Detection
#### About Dataset
#### Kaggle dataset credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase.
## ML-DVC-Pipeline
#### DVC 
#### Initialize a new Git repository:
`git init`
#### Initialize DVC in project directory:
`dvc init`
#### Add the data file to DVC:
`dvc add data.csv`
#### Add the DVC file and .gitignore to Git:
`git add .gitignore data.csv.dvc`
#
`git commit -m "Add data"` 

#### Configure a remote storage for DVC:
`dvc remote add -d storage gdrive://1W4VEkftEoGvWedVK1LSUEQuwEkrxdBcJ`
#
`git commit .dvc/config -m "Configure remote stroage"`
#### Pushes the tracked data files to the remote storage:
`dvc push`

#### DVC Pipeline Automate
`dvc run -n data -d get_data.py -o creditcard.csv --no-exec python get_data.py`
