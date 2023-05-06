# ML-DVC-Pipeline

git init
dvc init

dvc add data.csv
git add .gitignore data.csv.dvc
git commit -m "Add data"

dvc remote add -d storage gdrive://1W4VEkftEoGvWedVK1LSUEQuwEkrxdBcJ
git commit .dvc/config -m "Configure remote stroage"

dvc push
