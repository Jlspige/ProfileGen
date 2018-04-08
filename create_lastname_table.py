#!/usr/bin/env python
import sys

input_file = sys.argv[1]
read_file = open(input_file, 'r')
write_file = open('create_lastname_table.txt', 'w+')

file_content = "CREATE TABLE Lastnames (\n\tLastname Varchar(255)\n);\nINSERT INTO Lastnames\nVALUES\n"

for line in read_file:
    line = line.strip('\n')
    file_content += "\t('" + line + "'),\n"

file_content = file_content[:len(file_content) - 2] + ';'
write_file.write(file_content)
