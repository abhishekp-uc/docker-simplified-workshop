# set base image (host OS)
FROM python:alpine3.8

# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

#### These commands will make the build slow since dependencies are bigger in size
# install MySQL dependencies
RUN apk update
# Basic Necessary packages for build
RUN apk --no-cache add --virtual build-deps-alpine build-base
# For MySQL
RUN apk --no-cache add --virtual mysql-dependencies mariadb-dev
# API requirements - Note: We remove the requirements.txt file to decrease the size of the image
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /requirements.txt
# Challenge: You can additionally decrease the size of the docker image even still
# Hint: Base on installtion we can delete assests which are no longer required

# copy the content of the local src directory to the working directory in the image
COPY src/ .

# Run the application
CMD flask run --host=0.0.0.0