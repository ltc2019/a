#!/bin/bash
cd D:/JS/a
git add .
git commit -m "update"
git remote rm origin
git pull --a origin main
git remote add origin git@github.com:ltc2019/a.git
git push -u origin main