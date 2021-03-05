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
    cron \
    nano \
    libatlas-base-dev \
    && pip install --index-url=https://www.piwheels.org/simple -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

COPY crontab /etc/cron.d/velov-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/velov-cron

# Apply cron job
RUN crontab /etc/cron.d/velov-cron

COPY .  .

ENTRYPOINT [ "python","main.py" ]



