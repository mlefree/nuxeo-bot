# README #

> nuxeo bot server

based on https://github.com/revolutech/revolubot (fidj.ovh extended bot)

## Install

```bash
python3 -m venv .env/
# set this env as your main interpreter
pip3 install --upgrade -r requirements.txt
```

    
### Launch


```bash
nohup gunicorn web:app --log-file=- --reload &
```
    
   
### Variables to set

* FIDJ_APP_ID = 
* FIDJ_SECRET_KEY = 
    
go into [BOT@7654](http://localhost:7654)
