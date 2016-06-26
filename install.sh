#!/bin/bash

virtualenv -p $(which python3) .
source bin/activate
pip install -r requirements.txt
