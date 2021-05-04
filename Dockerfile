FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt /app/
WORKDIR /app/
RUN python -m pip install -r requirements.txt

COPY ./app /app/app

ENV APP_MODULE=app.main:app

ENV SECRET_KEY=${SECRET_KEY}
ENV ALGORITHM=${ALGORITHM}
ENV DEFAULT_USER=${DEFAULT_USER}
ENV DEFAULT_PASSWORD=${DEFAULT_PASSWORD}
ENV DATABASE_URL=${DATABASE_URL}