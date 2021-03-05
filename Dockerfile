FROM python:3.7-slim

USER root

WORKDIR /usr/app/

COPY requirements.txt .

#Instructions needed to install numpy on ARM distrib:
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    make \
    gcc \
    git \
    libatlas-base-dev \
    && pip install --index-url=https://www.piwheels.org/simple -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


COPY .  .

ENTRYPOINT [ "python","main.py" ]



