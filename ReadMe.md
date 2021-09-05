# AVIYEL CONFERENCE MANAGER

Manage Conference, Talks. Participants, Speakers 

### https://ancient-garden-72763.herokuapp.com/docs

Installation & Setup
=======================================================

1. Create vritual env in the root folder of project

     `python -m venv aviyel-conference`
2. Create a .env file with below contents, also create local database as mentioned in the below update connection string accordingly

     ``` 
      API_V1_STR=/api/v1
      PROJECT_NAME=Aviyel Conference Manager

      # Postgres Section
      SQLALCHEMY_DATABASE_URI=postgresql://postgres:MyPassword123456@localhost/conference

     ```
3. Update the Connection string for `SQLALCHEMY_DATABASE_URI`
4. Also Update the migration connection string in alembic.ini in the root folder 

     ```
    # the output encoding used when revision files
    # are written from script.py.mako
    # output_encoding = utf-8

    sqlalchemy.url = postgresql://postgres:MyPassword123456@localhost/conference
   
    ```
5. Intstall pip packages

    `pip install -r requirements.txt`

6. Run Migration with alembic

    `alembic upgrade head`
    
7. Run the application using below command

    `hypercorn main:app --reload`
    
API Docs & Swagger
=======================================================
Once application is running, please check the url http://127.0.0.1:8000/docs
![image info](./docs/aviyel-conference-manager-swagger.PNG)



Deployed on Heroku with Postgres & API
=======================================================

Please check the deployed version

https://ancient-garden-72763.herokuapp.com/docs

Consider the Heroku has no context warmup , so it might be slow for the initial time and database ins not the perfromant. 
This is just demonstration purpose



