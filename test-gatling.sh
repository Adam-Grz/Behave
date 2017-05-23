#!/bin/bash

docker run -it --rm denvazh/gatling
docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala
ls
./gatling.sh
