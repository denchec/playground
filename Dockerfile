FROM python:3.11-bullseye

RUN mkdir /backend

WORKDIR /backend

COPY . /backend/

RUN apt-get update
RUN apt-get upgrade -y pip
RUN apt-get upgrade -y vim
#RUN apt-get install -y postgresql gcc g++ musl-dev python3-dev

RUN pip install --no-cache-dir -r requirements.txt

#CMD python /backend/main.py
