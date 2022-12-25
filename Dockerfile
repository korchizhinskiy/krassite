FROM python:3.11-alpine

MAINTAINER Korchizhinskiy Nazar

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user

USER user
