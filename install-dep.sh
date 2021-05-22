#!/bin/bash

apt update
apt install -y python3-opencv
apt install -y ghostscript python3-tk


pip install --upgrade pip
pip install -r /requirements.txt  

