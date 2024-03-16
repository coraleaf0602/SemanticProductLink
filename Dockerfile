FROM python:3.9-alpine
RUN mkdir -p /usr/src/app
COPY ./* /usr/src/app/
WORKDIR /usr/src/app     
RUN pip install Flask flask-cors requests
CMD python backend.py

