#!/usr/bin/env python 

import csv
import string
import random
import sys

from cmscontrib.AddUser import add_user
from cmscontrib.AddParticipation import add_participation

csv_file = open("users.csv", "r") 
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)


CONTEST1_ID = int(sys.argv[1])
CONTEST2_ID = int(sys.argv[2])
CONTEST3_ID = int(sys.argv[3])

for row in csv_reader: 
    first_name, last_name, email, username, password_day1, password_day2, password_day3 = row
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
                        hidden = False, \
                        unrestricted = False)
    add_participation(username = username, \
                        contest_id = CONTEST3_ID, \
                        ip = None, \
                        delay_time = 0, \
                        extra_time = 0, \
                        password = password_day3, \
                        method = "plaintext", 
                        is_hashed = False, \
                        hidden = False, \
                        unrestricted = False)


