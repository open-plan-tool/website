#!bin/bash

git checkout main
git pull
git checkout static_website
git merge main
python create_static_website.py
git add *.html
git commit -m "Update website"
git push