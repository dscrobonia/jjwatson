from bs4 import BeautifulSoup
import requests

PROJ_STATS_FILE = "proj_stats_wk{0}.csv"
CURRENT_WEEK_URL = 'http://www.fantasypros.com/nfl/projections/{0}.php?export=xls&week={1}'
'http://www.fantasypros.com/nfl/projections/qb.php?filters=71:73&export=xls&week=9'

if (getCurrentWeek):
   #get html for CURRENT_WEEK_URL
   response = requests.get(CURRENT_WEEK_URL)

   with open(FD_PRICES_FILE, 'w') as outFile:
      start_ndx = response.text.find("GID")
      end_ndx = response.text.find("<center><script type=")

      csv = response.text[start_ndx: end_ndx]
      print csv

      outFile.write(csv)

if (getHistoricalWeek):
   for i in range(1,7):
      #get html for CURRENT_WEEK_URL
      response = requests.get(HISTORICAL_WEEK_URL.format(str(i)))
      file_str = FD_PRICES_HIST_FILE.format(str(i))

      with open(file_str, 'w') as outFile:
         start_ndx = response.text.find("Week;Year;GID;Name;Pos;Team;h/a;Oppt;FD points;FD salary")
         end_ndx = response.text.find("</pre>\n<!--- BOTTOM BOILERPLATE")

         csv = response.text[start_ndx: end_ndx]
         print csv

         outFile.write(csv)
