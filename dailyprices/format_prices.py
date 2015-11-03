import csv

with open('fdprices.csv', 'rb') as inFile:
   with open('players.csv', 'wb') as outFile:
      csvReader = csv.reader(inFile, delimiter=';')
      csvWriter = csv.writer(outFile)

      for row in csvReader:
         if int(row[6]) > 0:
            csvWriter.writerow([' '.join(row[2].split(', ')[::-1]), row[1], row[10], row[6]])
