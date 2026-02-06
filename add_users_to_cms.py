#!/usr/bin/env python 

import csv
import string
import random
import sys

from cmscontrib.AddUser import add_user

csv_file = open("users.csv", "r") 
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

# Create teams
team = {
    "Class 7": "class7",
    "Class 8": "class8",
    "Class 9": "class9",
    "Class 10": "class10",
    "Class 11": "class11", 
    "Class 12/HSC 2026": "hsc", 
    "SSC 2026 Candidates": "ssc", 
    "Others": "others"
}
for row in csv_reader: 
    first_name, last_name, grade, email, username, password = row
    add_user(first_name = first_name, \
             last_name = last_name, \
             username = username, \
             password = password, \
             method = "plaintext", \
             is_hashed = False, \
             email = email, \
             timezone = "Asia/Dhaka", \
             preferred_languages = "")


