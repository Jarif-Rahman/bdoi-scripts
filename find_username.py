import sys
import csv

csv_file = open("users.csv", "r") 
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

emails = []

if sys.argv[1] == 'file':
    emails = [x.strip() for x in open(sys.argv[2], 'r').read().split('\n')]
else:
    emails = [sys.argv[1]]

for row in csv_reader:
    first_name, last_name, grade, email, username, password = row
    if email in emails: 
        print(username)
