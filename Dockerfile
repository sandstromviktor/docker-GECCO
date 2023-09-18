FROM python:3.8-slim

ENV USER=gecco
ENV HOME=/home/$USER


RUN apt-get update -yq \
    && useradd -m $USER \
    && pip install --upgrade --no-cache-dir pip 

RUN apt-get install -y --no-install-recommends git \
    vim \
    && apt-get purge -y --auto-remove

COPY requirements.txt requirements.txt

RUN git clone https://github.com/zellerlab/GECCO.git
RUN pip install -r requirements.txt --no-cache-dir
RUN chown -R $USER:$USER $HOME 
RUN rm -rf /var/lib/apt/lists/* requirements.txt

COPY app.py $HOME/app.py
USER $USER
EXPOSE 8080
WORKDIR $HOME
CMD gradio app.py
