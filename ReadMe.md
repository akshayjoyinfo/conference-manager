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
