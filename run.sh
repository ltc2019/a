#!/bin/bash
cd D:\JS\all
git add .
#git commit -m "update"
#git commit --amend --date=now
git commit --amend --date="now"
git remote rm origin
git remote add origin git@github.com:ltc2019/a.git
git remote add origin git@github.com:ltc2019/a.git
git pull --a origin main
git push -u origin main