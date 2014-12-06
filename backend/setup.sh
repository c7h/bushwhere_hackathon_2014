#!/bin/bash

# Setup venv
virtualenv venv
source venv/bin/activate

# Install Django and Django REST framework into the virtualenv
pip install -r requirements.txt
