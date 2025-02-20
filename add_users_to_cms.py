#!/usr/bin/env python 

import csv
import string
import random
import sys

from cmscontrib.AddUser import add_user, add_participation

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
    "Class 12/HSC 2025": "hsc", 
    "SSC 2025 Candidates": "ssc", 
    "Others": "others"
}


CONTEST1_ID = int(sys.argv[1])
CONTEST2_ID = int(sys.argv[2])

for row in csv_reader: 
    first_name, last_name, grade, email, username, password_day1, password_day2 = row
    add_user(first_name = first_name, \
             last_name = last_name, \
             username = username, \
             password = password_day1, \
             method = "plaintext", \
             is_hashed = False, \
             email = email, \
             timezone = "Asia/Dhaka", \
             preferred_languages = "")
    add_participation(username = username, \
                        contest_id = CONTEST1_ID, \
                        ip = None, \
                        delay_time = 0, \
                        extra_time = 0, \
                        password = password_day1, \
                        method = "plaintext", 
                        is_hashed = False, \
                        team_code = team[grade], \
                        hidden = False, \
                        unrestricted = False)
    add_participation(username = username, \
                        contest_id = CONTEST2_ID, \
                        ip = None, \
                        delay_time = 0, \
                        extra_time = 0, \
                        password = password_day2, \
                        method = "plaintext", 
                        is_hashed = False, \
                        team_code = team[grade], \
                        hidden = False, \
                        unrestricted = False)


