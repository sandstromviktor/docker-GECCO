FROM python:3.8-slim

ENV USER=gecco
ENV HOME=/home/$USER


RUN apt-get update -yq \
    && useradd -m $USER \
    && pip install --upgrade --no-cache-dir pip 

RUN apt-get install -y --no-install-recommends git \
    vim \
    && apt-get purge -y --auto-remove


WORKDIR $HOME
RUN git clone https://github.com/zellerlab/GECCO.git
RUN pip install gecco-tool
RUN chown -R $USER:$USER $HOME 

RUN rm -rf /var/lib/apt/lists/*
USER $USER
EXPOSE 8000
