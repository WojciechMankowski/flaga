import os

os.system("git fetch origin")
os.system("git reset --hard origin/master")
os.system("git fetch")
os.system("git pull")