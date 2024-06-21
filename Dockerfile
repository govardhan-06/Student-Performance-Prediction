#getting the linux base image
FROM python:3.8-slim-buster

#creating app directory
WORKDIR /app 

#copying contents from current dir to app dir
COPY . /app

#updating packages
RUN apt update -y

#installing package
RUN pip install -r requirements.txt

#Running these commands while starting the container
CMD ["python3","app.py"]
