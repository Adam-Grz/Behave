#!/bin/bash

docker run -i -t themcmurder/ubuntu-python-pip /bin/bash
ls
pip -q install selenium requests behave promise git
git clone -q https://github.com/hugeinc/behave-parallel
cd behave-parallel
python setup.py --quiet install
cd ..
scennumber=$(sed 's/Scenario:/Scenario:\'$'\n/g' features/*.feature | grep -c "Scenario:")

#Running the test suite; results are created in TestResults directory
python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory TestResults

#Executing the brute force attack
docker cp bruteforce.py themcmurder/ubuntu-python-pip:/bruteforce.py
docker cp logins.txt themcmurder/ubuntu-python-pip:/logins.txt
docker cp passwords.txt themcmurder/ubuntu-python-pip:/passwords.txt
python bruteforce.py $TARGET_URL $LOGINS $PASSWORDS
