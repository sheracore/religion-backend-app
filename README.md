## Multi-scanner manager node

Manager node can receive input file either via URL or an API. The file will be sent to multiple agents and manager will gather interpreted results from agents.

## Using Docker-Compose
In order to use docker-compose, please add the following lines to `/etc/docker/daemon.json`: 
```
{
  "insecure-registries" : ["gitlab.fwutech.com:2222"]
}
```
Then, restart your docker service via: `service docker restart`

Done.
Start your service with `docker-compose up` OR `./docker-compose-up.sh`

## Installing Trid

Trid should be downloaded from front link : http://mark0.net/download/trid_linux.zip and followin command should be done:

    chmod +x ~/Path/To/trid
    sudo ln -s ~/Path/To/trid /usr/bin/trid
    sudo ln -s ~/Path/To/triddefs.trd /usr/bin/triddefs.trd



## Setup
Manager needs the following applications to run:
  - Python3.*
 - Postgresql
 - Redis

Python dependencies can be found in requirements.txt file and can be installed with the following command:

    $ pip install -r requirements.txt
   
 Configuration file can be found in **application/config**.py file. Database access should be created according to this file.

**Commands:**
Database migration:

    $ python manage.py db init
	$ python manage.py db migrate
	$ python manage.py db upgrade
	$ python manage.py db --help

To sync list of agents and check their status:

    $ python manage.py sync


  ## set settings :
  
    $ python manage.py create_setting

## Running manager

Manager runs scan jobs in the background using celery so for running the manager we need to run two commands:

    $ gunicorn --workers 16 --bind 0.0.0.0:8080 deploy:app
    
    $ celery worker -A celery_worker.celery -B --loglevel=info

 


##################### 
comment this line in application/app.py :
line(34)
 get_config_args(app)

run these command :
    python3 manage.py create_db
    python3 manage.py create_user admin admin admin@yahoo.com
    create_email_user

    if you want to active imap :
    in setting.json :
    "email_client_enabled": true

    python3 manage.py create_setting


reComment this line in application/app.py :
line(34)
 get_config_args(app)

run project
and celery
