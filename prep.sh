#!/bin/bash

docker pull themcmurder/ubuntu-python-pip
docker pull webgoat/webgoat-7.1
docker pull denvazh/gatling:latest

docker run -d -p 8080:8080 -t webgoat/webgoat-7.1
