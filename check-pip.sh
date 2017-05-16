#!/bin/bash
if [ ! -f /usr/local/lib/python2.7/site-packages/pip ]; then
	python get-pip.py
else
	echo "\n\t\tPip already installed\n"
fi
