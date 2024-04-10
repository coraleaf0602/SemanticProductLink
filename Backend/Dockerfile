FROM python:3.11
RUN mkdir -p /usr/src/app
COPY ./* /usr/src/app/
WORKDIR /usr/src/app     
RUN pip3 install -r requirements.txt
ENV API_KEY="0088e713d9044d72a48f7c468a12aa6b"
EXPOSE 50505
ENTRYPOINT [ "gunicorn","backend:app" ]

