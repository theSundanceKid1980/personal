import csv
import sys

with open(sys.argv[1], newline='') as infile:
    reader = csv.reader(infile)
    linecount = 0
    with open('output.csv', mode='w') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        for row in reader:
            if linecount == 0:
                print(f'Column names are {", ".join(row)}')
                print('There are ',len(row), 'columns.')
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12], row[13], row[14], row[15], row[16]])
                linecount += 1
            elif len(row) == 17:
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12], row[13], row[14], row[15], row[16]])
            elif len(row) > 17 and row[14] == 'Posted' and row[12] == 'NULL':
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10] + row[11],row[12], row[13], row[14], row[15], row[16], row[17]])
                linecount += 1
            elif len(row) > 17 and row[14] == 'Posted' and row[12] != 'NULL' and row[11] == 'NULL':
                writer.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12] + row[13], row[14], row[15], row[16], row[17]])
                linecount += 1
        print('The total number of lines is ', linecount)

