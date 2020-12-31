# **PYTHON - REACT** MICROSERVICES

This app is an aproach to microservices using python  
microservices are smaller independant applications or services that are able to cominicate between them  
throug the use of an event bus using messages, each one of them has its own database.  

## **Django rest framework** as microservice 1
a backend microservice running in **docker**, managing data in **mysql** database  
comunicates with microservice 2 using **RabbitMQ** events 

**products views**  

> /admin/products
- shows all products information located in the database

> /admin/products/create  
- allows creation of a new product filling the tittle and image-link field

> /admin/products/<str:id>/edit  
- allows to update tittle and image of the product

> /admin/products/<str:id>/delete
- allow deletion of a product based on its id

**user views**  

> /api/user
- represents user views from database
  generates random users id, this random user is able to like products  

**Required packages**  

django==3.1.3  

djangorestframework==3.12.2  

mysqlclient==2.0.1  

django-mysql==3.9  
 
django-cors-headers==3.5.0  

pika==1.1.0  


## **flask microframework** as microservice 2  
a backend microservice running in **docker**, managing data in **mysql** database
comunicates with microservice 1 using **RabbitMQ** events

> /api/products/  
- shows a list of products with its properties  

> /api/products/<int:id>/like  
- adds a like wich is incremented in the database

## Required packages  

Flask==1.1.2  

Flask-SQLAlchemy==2.4.4  

SQLAlchemy==1.3.20  

Flask-Migrate==2.5.3  

FlaskScript==2.0.6  

FlaskCors==3.0.9  

requests==2.25.0  

mysqlclient==2.0.1  

pika==1.1.0


## **React** as frontend  

- used to develop a user interface in this project

## **Mysql** as database  

**django models**  
- - title : max lenght(200)
- - image : max lenght(200)
- - likes : default(0)


**flask models**  

- **Product model**  
- - id : default(pk)
- - title : max lenght(200)
- - image : max lenght(200)  

- **User's Product model**  
- - id : default(pk)
- - user_id : max lenght(200)
- - product_id : max lenght(200)


## **RabbitMQ** as broker

- allows communication through messages between services in the backend,  
this means in this case we can keep synchronized both databases on every  
event no matter in which one occurs that event  






