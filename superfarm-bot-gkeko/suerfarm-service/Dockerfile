FROM python:3.6-stretch
LABEL maintainer "George Fiotakis, gfiotakis@core-innovation.com" 

COPY ./app /app

RUN apt-get install libssl-dev libffi-dev
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["gunicorn", "-c", "gunicorn_config.py", "wsgi:app" ]
