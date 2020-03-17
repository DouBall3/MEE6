FROM python:alpine

WORKDIR /srv/meesix

RUN apk update && apk upgrade
RUN apk add linux-headers build-base
RUN pip install uwsgi

COPY *.py ./
COPY requirements.txt .
COPY chatac.json .

RUN pip install -r requirements.txt

RUN ["python", "bot.py"]

EXPOSE 8080

