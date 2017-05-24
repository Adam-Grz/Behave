#!/bin/bash
scennumber=$(sed 's/Scenario:/Scenario:\'$'\n/g' features/*.feature | grep -c "Scenario:")
