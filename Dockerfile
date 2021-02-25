FROM python:3.8-slim

USER root

WORKDIR /usr/app/
CMD mkdir data
CMD mkdir logs

COPY requirements.txt .

RUN apt update && apt-get install -y libffi-dev
RUN pip install -r requirements.txt

COPY .  .




