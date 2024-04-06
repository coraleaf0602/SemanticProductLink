FROM python:3.11
RUN mkdir -p /usr/src/app
COPY ./* /usr/src/app/
WORKDIR /usr/src/app     
RUN pip3 install -r requirements.txt
EXPOSE 50505
ENTRYPOINT [ "gunicorn","backend:app" ]

