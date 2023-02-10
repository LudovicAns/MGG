#!/bin/bash

# Path to MGG
cd /home/edenthread/Documents/MGG/

cd ./.venv/bin/
. ./activate
python ./MGG.py
git add Messages\ from\ openAI.txt
git commit -m "🌴 Making Github Greener !"
git push origin master
