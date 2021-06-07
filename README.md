# ieee-docker-workshop

## Prerequisites
### Download / Pull the MySQL DB image
```shell
$ docker pull mysql:8.0
8.0: Pulling from library/mysql
69692152171a: Pulling fs layer 
1651b0be3df3: Pulling fs layer 
951da7386bc8: Pulling fs layer 
0f86c95aa242: Waiting 
37ba2d8bd4fe: Waiting 
6d278bb05e94: Waiting 
497efbd93a3e: Pull complete 
f7fddf10c2c2: Pull complete 
16415d159dfb: Pull complete 
0e530ffc6b73: Pull complete 
b0a4a1a77178: Pull complete 
cd90f92aa9ef: Pull complete 
Digest: sha256:d50098d7fcb25b1fcb24e2d3247cae3fc55815d64fec640dc395840f8fa80969
Status: Downloaded newer image for mysql:8.0
docker.io/library/mysql:8.0
```

### Download / Pull the Python 3.8 image
```shell
$ docker pull python:alpine3.8
alpine3.8: Pulling from library/python
c87736221ed0: Already exists 
c3f51b0d0765: Already exists 
a65abebf5480: Pull complete 
6628a73c2c85: Pull complete 
b49d22f17d2f: Pull complete 
Digest: sha256:3491d1abd29b3f87ca5cb1afd34bc696855a2403df1ff854da55cb6754af1ff8
Status: Downloaded newer image for python:alpine3.8
docker.io/library/python:alpine3.8:8.0
```
---
## Learning Docker Docker Basics
### Build the contianer docker image
```shell
$ docker build -t ieee-docker-workshop-python-image .
Sending build context to Docker daemon  77.82kB
Step 1/6 : FROM python:alpine3.8
 ---> f11f279751de
Step 2/6 : WORKDIR /code
 ---> Using cache
 ---> b2e7220c5d01
Step 3/6 : COPY requirements.txt .
 ---> Using cache
 ---> b3145ab9c4e0
Step 4/6 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 6c3e97eebf72
Step 5/6 : COPY src/ .
 ---> Using cache
 ---> 88079192aaf8
Step 6/6 : CMD [ "python", "./server.py" ]
 ---> Using cache
 ---> 0bfb3b596768
Successfully built 0bfb3b596768
Successfully tagged ieee-docker-workshop-python-image:latest
```

### List the docker images
```shell
$ docker images
REPOSITORY                               TAG                     IMAGE ID            CREATED             SIZE
ieee-docker-workshop-python-image        latest                  0bfb3b596768        21 minutes ago      89.9MB
```

### Run the container
```shell
$ docker run --name ieee-docker-workshop-python-container -d -p 5000:5000 ieee-docker-workshop-python-image
a1804f7de9ca9309b91e68f4918023526d973617702e616f50336db0d482d9e4
#     --name string      Assign a name to the container
# -d, --detach           Run container in background and print container ID
# -p, --publish list     Publish a container's port(s) to the host
# You can even combine flags like '-d' & '-p' as '-dp'
```

### Check the processes running
```shell
$ docker container ls
CONTAINER ID        IMAGE                               COMMAND                  CREATED             STATUS              PORTS                    NAMES
a1804f7de9ca        ieee-docker-workshop-python-image   "python ./server.py"     24 seconds ago      Up 23 seconds       0.0.0.0:5000->5000/tcp   ieee-docker-workshop-python-container
# The output below is only different for the NAMES field which is to showcase what would've happened if --name was not provided in the previous step
# a1804f7de9ca      ieee-docker-workshop-python-image   "python ./server.py"     24 seconds ago      Up 23 seconds       0.0.0.0:5000->5000/tcp   zen_khayyam
```

### Check the processes running
```shell
$ docker exec -it ieee-docker-workshop-python-container sh
/code # python
Python 3.7.3 (default, Mar 27 2019, 23:51:31) 
[GCC 6.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```


### Build the containers using the docker compose file
```shell
$ docker-compose up -d
Creating network "ieee-docker-workshop_backend-network" with the default driver
Creating network "ieee-docker-workshop_frontend-network" with the default driver
Creating project-mysql-db        ... done
Creating project-python3-backend ... done
```

### Attach to the database container
```shell
$ docker exec -it project-mysql-db bash
root@5e4a7a145009:/# docker exec -it project-mysql-db bash
bash: docker: command not found
root@5e4a7a145009:/#  mysql -uroot -ppassword
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.25 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------------+
| Database                 |
+--------------------------+
| ieee_project_application |
| information_schema       |
| mysql                    |
| performance_schema       |
| sys                      |
+--------------------------+
5 rows in set (0.00 sec)

mysql> use ieee_project_application;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+------------------------------------+
| Tables_in_ieee_project_application |
+------------------------------------+
| users                              |
+------------------------------------+
1 row in set (0.01 sec)

mysql> select * from users;
+----+------------+-----------+----------------+------+
| id | first_name | last_name | cell_phone     | age  |
+----+------------+-----------+----------------+------+
|  1 | Linus      | Trovaldus | +91-1234567890 |   19 |
|  2 | Dennis     | Richie    | +91-8596471350 |   21 |
+----+------------+-----------+----------------+------+
2 rows in set (0.00 sec)

mysql>
```