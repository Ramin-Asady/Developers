FROM python:3.10.11-slim-buster

WORKDIR /code

COPY requirements.txt  .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver" , "0.0.0.0:3000"]