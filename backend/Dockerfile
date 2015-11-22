# This starts the api in a docker container using the `python` base image
FROM python:3.5
ADD . /api
WORKDIR /api
RUN pip3 install -r requirements.txt
CMD `which gunicorn` --bind 0.0.0.0:80 api:app --log-level INFO --threads 8 --log-file=-
