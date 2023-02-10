#!/bin/bash

# Path to MGG
cd ~/Documents/VSCode/MGG/

source ./.venv/bin/activate
python ./MGG.py
git add Messages\ from\ openAI.txt
git commit -m "🌴 Making Github Greener !"
git push origin master