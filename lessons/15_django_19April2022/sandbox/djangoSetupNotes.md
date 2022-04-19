#interesting ref: https://docs.djangoproject.com/en/3.1/intro/tutorial01/


## upgrade pip
pip install --upgrade pip

## MacOS
python3 -m venv myvenv
 -or-
 pip3 install virtualenv
 virtualenv myenv -p python3.6
source myenv/bin/activate
pip3 install django


### Linux
python3 -m venv myvenv
 -or-
# pip install virtualenv
# virtualenv myenv -p python3
source myenv/bin/activate
pip install django


### Windows
python3 -m venv myvenv
 -or-
# pip install virtualenv
# virtualenv myenv -p python3
cd myenv/Scripts/
run: activate
pip install django



### commands to run django project
python3 -m django --version
django-admin startproject mysite
cd mysite
python3 manage.py runserver
