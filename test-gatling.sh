#!/bin/bash

docker cp RecordedSimulation.scala denvazh/gatling:/RecordedSimulation.scala
docker run -it -m denvazh/gatling /bin/bash
ls
./gatling.sh
