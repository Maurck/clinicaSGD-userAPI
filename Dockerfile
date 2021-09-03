FROM python:3.9.1
ADD . /sgd-users
WORKDIR /sgd-users
RUN pip install -r requirements.txt