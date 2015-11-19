import csv
import requests

positions = ['qb', 'wr', 'rb', 'te']
PROJ_STATS_FILE = "proj_stats_wk{0}.csv"
CURRENT_WEEK_URL = 'http://www.fantasypros.com/nfl/projections/{0}.php?export=xls&week={1}'

#FD_PRICES_HIST_FILE = "fd_prices_hist_wk{0}.csv"
#HISTORICAL_WEEK_URL = 'http://rotoguru1.com/cgi-bin/fyday.pl?week={0}&game=fd&scsv=1'

getCurrentWeek = True
getHistoricalWeek = not getCurrentWeek

if (getCurrentWeek):
   with open(PROJ_STATS_FILE.format(str(11)), 'w') as outFile:
      csvWriter = csv.writer(outFile)

      #get data for each player
      for position in positions:
         response = requests.get(CURRENT_WEEK_URL.format(position, str(11)))

         csvReader = csv.reader(response.text.split('\n'), delimiter='\t')

         for i in range(0,6,):
            print csvReader.next()

         for row in csvReader:
            if row and row[1] != 'FA':
               csvWriter.writerow(row)

      #outFile.write(response)

if (getHistoricalWeek):
   for i in range(10,11):
      #get html for CURRENT_WEEK_URL
      response = requests.get(HISTORICAL_WEEK_URL.format(str(i)))
      file_str = FD_PRICES_HIST_FILE.format(str(i))

      with open(file_str, 'w') as outFile:
         start_ndx = response.text.find("Week;Year;GID;Name;Pos;Team;h/a;Oppt;FD points;FD salary")
         end_ndx = response.text.find("</pre>\n<!--- BOTTOM BOILERPLATE")

         csv = response.text[start_ndx: end_ndx]
         print csv

         outFile.write(csv)

