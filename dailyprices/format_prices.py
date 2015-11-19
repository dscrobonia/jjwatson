import csv
import sys

inFileName = ''
outFileName = ''
isHistorical = False

if len(sys.argv) > 1:
   inFileName = sys.argv[1]
   outFileName = sys.argv[2]

with open(inFileName, 'rb') as inFile:
   with open(outFileName, 'wb') as outFile:
      csvReader = csv.reader(inFile, delimiter=';')
      csvWriter = csv.writer(outFile)

      line1 = next(csvReader)

      #historical
      if line1[0] == 'Week':
         for row in csvReader:
            if row[9]:
               csvWriter.writerow([' '.join(row[3].split(', ')[::-1]), row[4], row[8], row[9]])

      #current week
      elif line1[0] == 'GID':
         for row in csvReader:
            if int(row[6]) > 0:
               csvWriter.writerow([' '.join(row[2].split(', ')[::-1]), row[1], row[10], row[6]])
