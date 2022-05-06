FROM python:3.10


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/fastapi

RUN pip install pipenv
COPY Pipfile Pipfile.lock /usr/src/fastapi/
RUN pip install psycopg2-binary
RUN pipenv install --system --dev


COPY . /usr/src/fastapi

EXPOSE 8000