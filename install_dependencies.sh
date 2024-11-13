#! /bin/sh

# Read requirements from project and generate requirements.txt
pipreqs --mode gt --force .

# Install requirements
pip install -U -r requirements.txt