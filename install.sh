#!/bin/sh
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt install python3-pip
pip3 install requests web3 mnemonic 
curl -o- -k https://raw.githubusercontent.com/IsoumaDev/PythonA/refs/heads/main/test.py > test.py
