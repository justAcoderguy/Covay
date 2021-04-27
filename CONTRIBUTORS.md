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
  - Once you have created .env file, please adhere to the .env.example file in mysite/.env.example present to fill in the values.
  - GOOGLE_MAPS_API_KEY is not required if you dont want to see the working maps. If you have an API key at your disposal , feel free to use it
    It is however not necessary and you should still be able to see the outline of the map for styling purposes
  - Make sure DEBUG is set to True
  - Make sure you provide a valid Django Secret Key.

2. Create a Virtual Environment in the Root directory and activate it( directory with manage.py ).
(Code for linux OS):
```
python -m venv venv
source venv/bin/activate
```
3. Install requirements.
```
pip install -r requirements.txt
```
4. Make some changes in your settings.py file.
  - Go to the database section and uncomment the db.sqlite3 config.
  - Comment out the postgresql config
  - **MAKE SURE TO REVERT THIS CHANGE BEFORE PUSHING**
5. Run migrate command
```
python manage.py migrate
```
