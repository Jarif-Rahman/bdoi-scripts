import csv
import sys
import random
import string

csv_file = open("users.csv", "w") 
csv_writer = csv.writer(csv_file, delimiter=',')

csv_writer.writerow(["first_name", "last_name", "email", "username", "password_day1", "password_day2", "password_day3"])

random.seed(int(sys.argv[1]))

rawFile = open(sys.argv[2], "r") #format: email, first_name, last_name, ...
rawFileReader = csv.reader(rawFile, delimiter=',')
next(rawFileReader)

count = 1

for row in rawFileReader:
    email, first_name, last_name = row[3:7]
    username = f"u{count:02d}"
    count += 1
    password_day1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    password_day2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    password_day3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    csv_writer.writerow([first_name, last_name, email, username, password_day1, password_day2, password_day3])