# #Initial template
FROM ubuntu:18.04

# #Install apache web server
# RUN apt update && apt install -y --no-install-recommends apache2
# # Install php and apache web server
FROM php:7-apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
COPY . /var/www/html/

# # Install Mysql server
# FROM mysql:5.6
# ENV MYSQL_DATABASE=root
# ENV MYSQL_ROOT_PASSWORD root

# #Install python and libraries used
# FROM python:2.7
RUN apt-get update
# RUN apt-get install python
# RUN pip install requests
# RUN pip install mysql-connector
# RUN pip install paho-mqtt
# copy ./project /var/www/html
# # WORKDIR /var/project
# RUN ls
# # RUN ls usr/sbin/
# # Expose port
# EXPOSE 80/tcp
# CMD ["python","seed.py"]
# CMD ["python","mqtt.py"]
# ENTRYPOINT ["apache2","-D","FOREGROUND"]
# ENTRYPOINT ["/usr/sbin/apache2ctl","-D","FOREGROUND"]
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
#Initial template
# FROM ubuntu:18.04
# FROM php:7.2-apache
# #Install apache web server
# # RUN apt update && apt install -y --no-install-recommends apache2

# #Files to copy into the container
# RUN ls
# COPY ./project/ /var/www/html/

# FROM python:3
# RUN pip install requests
# RUN pip install mysql-connector
# RUN pip install paho-mqtt
# RUN pwd
# RUN ls /var/
# RUN ls /var/www/html/scripts/
# WORKDIR /var/scripts/
# CMD ["python","seed.py"]
# CMD ["python","mqtt.py"]
#Ports to allowed out
EXPOSE 80/tcp
# RUN pwd
#The entry point to run from
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]