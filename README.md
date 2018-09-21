# README #

based on https://github.com/revolutech/revolubot

### Install
    # done with : python3 -m venv env-bot
    source ../env-bot/bin/activate
    pip3 install -r requirements.txt
    
    # pip freeze > requirements.txt
    
### Launch


    nohup gunicorn app:app &
    
    nohup gunicorn web:app --log-file=- --reload &
    
   
### Variables to set

* FIDJ_APP_ID = 
* FIDJ_SECRET_KEY = 
    
go into [BOT@7654](http://localhost:7654)
