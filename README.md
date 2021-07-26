About the service.

Users can write a review to some online shop, providing: 

    • Full ecommerce link 
    • Review title
    • Review text
    • Stars count (from 1 to 5)
    • Reviews author email

Only authorized users can use the service.
The service provides the following functionality to the user:

    • add review
    • update review (only review's author or admin can update it)
    • delete review (only review's author or admin can delete it)
    • get shop list order by rating or review count
    • get group by user email reviews order by creating time 
    • get one shop by domain name
    
    
Running the service.

Clone and pull the following repo:
https://github.com/andrew030987/eshop_quality_reviews.git

In the settings.py make sure your database configuration is as follows:

DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'test',
        'HOST': 'db',
        'PORT': '5432',
    }
    }
    
    
Now you can up the project in Docker container. Type in terminal:

    • sudo docker-compose up
    
Before service starts it will make migrations and run unit tests.

You will need to create a superuser with the following command:

    • docker-compose run web python manage.py createsuperuser


