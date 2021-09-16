# Bradoo Tech Test
Test for Python developer at Bradoo Tech

# Instructions

To run this project, the first thing you have to do, its to install the dependencies in your environment through the "requirements.txt" file, using the following command: 

### pip install -r requirements.txt

That being done, you have to modify the user and password of the postgres database, on the following files:

### vendors_catalogue/setting.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'username', <<
        'PASSWORD': 'pass', <<
        'HOST': 'database',
        'PORT': 5432,
    }
}
```
### docker-compose.yml

```
environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
```      

Then, you might have to make and execute the migrations. For that you will have to execute these commands:

```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```
After that, you can already run the local server, executing the following command:
```
docker-compose up
```
Then, the API will be able to test through the link: http://127.0.0.1:8000

It's noteworthy that docker and docker-compose must be installed on the PC, so that these commands above work.
