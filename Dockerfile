FROM python:3.7.0-alpine3.7

ENV FLASK_APP=fakeapp

COPY . /app

WORKDIR /app

RUN pip install --editable .

RUN flask

EXPOSE 5000


CMD [ "flask", "run", "--host=0.0.0.0" ]



