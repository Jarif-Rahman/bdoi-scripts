import csv
import sys
import random
import string

csv_file = open("users.csv", "w") 
csv_writer = csv.writer(csv_file, delimiter=',')

csv_writer.writerow(["first_name", "last_name", "grade", "email", "username", "password"])

random.seed(int(sys.argv[1]))

rawFile = open(sys.argv[2], "r") #format: email, first_name, last_name, grade, ...
rawFileReader = csv.reader(rawFile, delimiter=',')
next(rawFileReader)

count = 1

for row in rawFileReader:
    email, first_name, last_name, grade = row[:4]
    username = f"u{count:03d}"
    count += 1
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    csv_writer.writerow([first_name, last_name, grade, email, username, password])