# ML-DVC-Pipeline

## Initialize a new Git repository
# git init
## Initialize DVC in project directory
# dvc init
## Add the data file to DVC:
# dvc add data.csv
## Add the DVC file and .gitignore to Git:
# git add .gitignore data.csv.dvc
# git commit -m "Add data"
## Configure a remote storage for DVC:
# dvc remote add -d storage gdrive://1W4VEkftEoGvWedVK1LSUEQuwEkrxdBcJ

# git commit .dvc/config -m "Configure remote stroage"
## Pushes the tracked data files to the remote storage:
# dvc push
