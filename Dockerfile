FROM python:3.7-slim

USER root

WORKDIR /usr/app/

COPY requirements.txt .
COPY install_packages.sh .
#Instructions needed to install numpy on ARM distrib:
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    make \
    gcc \
    git \
    libatlas-base-dev \
    #To install package we run a script that accelerate installation on arm architectures:
    && chmod +x install_packages.sh &&  ./install_packages.sh \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


COPY .  .


ENTRYPOINT [ "python","main.py" ]



