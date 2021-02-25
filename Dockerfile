FROM python:3.8-slim

USER root

WORKDIR /usr/app/
CMD mkdir data
CMD mkdir logs

COPY requirements.txt .

#Instructions needed to install numpy on ARM distrib:
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    make \
    gcc \
    && pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY .  .




