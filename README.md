# Kidney disease 

# Workflow
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src  config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

'''
first clone
then create template.py and paste the content

use anaconda prompt for everything

then paste setup.py  --setup.py is the build script for setuptools, a Python package used to install your project as a packag

conda create -n kidney python=3.8 -y
conda activate kidney
pip install -r requirements.txt


add logging module in src
create  main.py and simply give welcome command
under utils add common.py
then under research open trial.py to download dataset

then follow the work flow after 1st go to research add data_ing
then go to constant --to get path of two yaml 
research data_ing - 4 5 6 7
then paste those thing seperate
add artifacts/* in gitignore

'''