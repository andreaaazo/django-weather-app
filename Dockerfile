FROM python:3.9.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /databerry_proj

COPY Pipfile Pipfile.lock /databerry_proj/

RUN pip install pipenv && pipenv install --system

COPY requirements.txt /databerry_proj/
RUN pip install -r requirements.txt

COPY . /databerry_proj/