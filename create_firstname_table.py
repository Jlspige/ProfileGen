#!/usr/bin/env python
import sys
import csv

input_file = sys.argv[1]
write_file = open('create_firstname_table.txt', 'w+')

file_content = "CREATE TABLE Firstnames (\n\tName Varchar(255),\n\tGender char(1),\n\tYear int(4)\n);\nINSERT INTO Firstnames\nVALUES\n"

with open(input_file, 'r') as read_file:
    reader = csv.reader(read_file)
    for line in reader:
        for i in range(1, 11):
            gender = ''
            if i < 6:
                gender = 'F'
            else:
                gender = 'M'
            file_content += "\t('" + line[i] + "', '" + gender + "', " + line[0] + "),\n"

file_content = file_content[:len(file_content) - 2] + ';'
write_file.write(file_content)
