FROM python:3.11-alpine
# RUN apt-get update -y
# RUN apt-get upgrade -y

ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY ./requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY . .

EXPOSE 8000

