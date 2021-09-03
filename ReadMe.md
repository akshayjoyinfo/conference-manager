Installation & Setup
=================================

python -m venv aviyel-conference

cd 
\Scripts\Activate


cd src\
pip install -r requirements.txt

API Docs
================================
http://127.0.0.1:8000/docs  -- Swagger API Doc


Migrations
===============================
alembic revision -m "Conference tables"

alembic upgrade head

run 

hypercorn main:app --reload

op.alter_column('talks', 'old_col_name', nullable=False, new_column_name='new_col_name')


Apply Migration Heroku before Deployment
=======================================
change DB connection before deployment

postgresql://postgres:MyPassword123456@localhost/conference
postgresql://swsyiowcohwxwa:8694f1638012477579400a476a034859c35664e599805ef453781eee2ef0928e@ec2-18-235-4-83.compute-1.amazonaws.com/dfm7rilqm8n17k



Applu db migration
alembic upgrade head



git add .
git push
git push heroku main


