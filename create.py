#! python3

import os
import sys
from github import Github

path = "E:/Repos/"
username = "18ucc104@lnmiit.ac.in"
password = "m1shra@2000"

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Successfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
