# set base image (host OS)
FROM python:alpine3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install MySQL dependencies
RUN apk update
# Basic Necessary packages for build
RUN apk --no-cache add --virtual build-deps-alpine build-base
# For MySQL
RUN apk --no-cache add --virtual mysql-dependencies mariadb-dev
# API requirements
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /requirements
## Deleting MySQL dependencies
#RUN apk del mysql-dependencies
## Deleting base dependencies
#RUN apk del build-deps-alpine

# copy the content of the local src directory to the working directory
COPY src/ .

# Run the application
#CMD flask run --host=0.0.0.0