#!/usr/bin/env python 

import csv
import sys

from cmscontrib.AddParticipation import add_participation

# Format: first_name, last_name, grade, email, username, password 
csv_file = open("users.csv", "r") 
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

CONTEST_ID = int(sys.argv[1])
emails = [x.strip() for x in open(sys.argv[2], 'r').read().split('\n')]

# Create teams
team = {
    "Class 7": "class7",
    "Class 8": "class8",
    "Class 9": "class9",
    "Class 10": "class10",
    "Class 11": "class11", 
    "Class 12/HSC 2024": "hsc", 
    "SSC 2024 Candidates": "ssc", 
    "Others": "others"
}

for row in csv_reader:
    first_name, last_name, grade, email, username, password = row
    if email in emails: 
        add_participation(username = username, \
                        contest_id = CONTEST_ID, \
                        ip = None, \
                        delay_time = 0, \
                        extra_time = 0, \
                        password = password, \
                        method = "plaintext", 
                        is_hashed = False, \
                        team_code = team[grade], \
                        hidden = False, \
                        unrestricted = False)



