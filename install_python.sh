#! /bin/sh

sudo apt update
sudo apt upgrade -y
sudo apt install python pip -y
pip install pipreqs
pip install -U packaging