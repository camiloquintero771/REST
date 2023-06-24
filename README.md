# API PROJECT
# Initial setup
You must create a file in the root of the project with the name .env with the following data:

### Django
DEBUG=True
SECRET_KEY='django-insecure-qzc%(1g4q$#3z$v1n+#bxxxq%04^(xm)f0mhbyt=d2ltvsrw0r'
TZ=America/Bogota    
DJANGO_SETTINGS_MODULE=restapi.settings.local
    
### Postgres    
POSTGRES_DB=restapi_db
POSTGRES_USER=restapi_user
POSTGRES_PASSWORD=restapi2021**.
POSTGRES_HOST=postgres    
POSTGRES_PORT=5432 
Then you must run the following command to build all the project containers:

$ make build
Finally you should generate the initial Django migrations, for them execute the following command

$ make migrate

Run project
To run the project you must execute the following command

$ make up

If you have problems connecting Django with Postgres, you should run the command: make restart CONTAINER=django

# Other commands
Create a new app: make startapp NAME=example
Generate migrations: make migrate
Create a superuser: make superuser
Sort packages in the requirements.txt file
First you need to add the package to the requirements.txt file, then you run the make build command. Finally, so that the packages are ordered and with their version established in the requirements.txt file, you must execute the following command.

$ make get-requirements
