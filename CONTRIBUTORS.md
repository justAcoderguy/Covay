# Covay - Contributors 
###### Please read this document before contributing

## Setting up the project on your local machine 

Once you have cloned (have contributing access) /cloned the fork of this repo ( do not have contributing access),
please follow the following steps :

1. Add a .env file in the 'mysite' app :
```
cd mysite
touch .env
```
For WINDOWS manually create .env in 'mysite' with some code editor like VS code
  - Once you have created .env file, please adhere to the .env.example file in mysite/.env.example present to fill in the values.
  - GOOGLE_MAPS_API_KEY is not required if you dont want to see the working maps. If you have an API key at your disposal , feel free to use it
    It is however not necessary and you should still be able to see the outline of the map for styling purposes
  - Make sure DEBUG is set to True
  - Make sure you provide a valid Django Secret Key.
  - Make sure your MODE is set to Local

2. Create a Virtual Environment in the Root directory and activate it( directory with manage.py ).
(Code for linux OS):
```
python -m venv venv
source venv/bin/activate
```
(Code for WINDOWS OS):
```
python3 -m venv venv
venv\Scripts\activate
```
3. Install requirements.
```
pip install -r requirements.txt
```
4. Run migrate command
```
python manage.py migrate
```
if this gives error "Path not defined" remove the BASE DIR code from local_settings.py also rename database to like 'db_name'

5.To start the development server
```
python manage.py runserver
```
6. Copy the URL and paste it in browser.

## Commmiting to this repo.
 1. While commiting please create a branch in your name/issue name and then commit. **DO NOT COMMIT TO MASTER BRANCH**
