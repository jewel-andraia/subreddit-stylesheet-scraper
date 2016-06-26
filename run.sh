#!/bin/bash

source bin/activate
python topsubreddits.py
python stylesheets.py
zip "stylesheets/stylesheets-$(date +%Y-%m-%dT%H-%M-%S).zip" stylesheets/*.css
