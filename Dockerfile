FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/
WORKDIR /app/
RUN python -m pip install -r requirements.txt

COPY ./app /app/app

ENV APP_MODULE=app.main:app