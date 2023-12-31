FROM python:3.10-slim-buster

# python 로그 설정
ENV PYTHONUNBUFFERED 1

RUN apt-get update
## gcc 설치(uWSGI 설치 시 필요)
RUN apt-get -y install gcc

COPY ./musicbox /musicbox
COPY requirements.txt /requirements.txt

WORKDIR /musicbox

RUN pip install --no-cache-dir --upgrade -r /requirements.txt