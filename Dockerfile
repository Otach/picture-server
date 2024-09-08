FROM python:latest

RUN apt update

RUN apt -y install python3-dev python3-pip

COPY requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

RUN mkdir /pictureserver

WORKDIR /pictureserver

EXPOSE 8000

ENTRYPOINT ["bash", "entrypoint.sh"]
