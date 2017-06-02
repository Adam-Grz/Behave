#!/bin/bash

Xvfb -ac :99 -screen 0 1280x1024x16 &
webdriver-manager start --standalone
