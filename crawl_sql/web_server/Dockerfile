FROM php:7-apache

WORKDIR /web-server
EXPOSE 80
COPY . .
RUN mv -f html/* /var/www/html
RUN docker-php-ext-install mysqli
