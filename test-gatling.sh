#!/bin/bash

docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala
docker run -it --rm denvazh/gatling /bin/bash
ls
./gatling.sh
