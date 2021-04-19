#!/bin/bash

sudo systemctl enable pigpiod
sudo systemctl start pigpiod

sudo apt-get install libatlas-base-dev
pip install numpy --upgrade
