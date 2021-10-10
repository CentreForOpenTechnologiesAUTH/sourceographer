#!/bin/bash

git clone https://github.com/chaoss/grimoirelab-perceval.git
cd ~/grimoirelab-perceval/
sudo pip3 install -r requirements.txt
sudo pip3 install .