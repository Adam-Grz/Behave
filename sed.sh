#!/bin/bash
scennumber=$(sed 's/Scenario:/Scenario:\'$'\n/g' features/*.feature | grep -c "Scenario:")
python behave-parallel/bin/behave-parallel --processes $scennumber --junit --junit-directory PythonResults
