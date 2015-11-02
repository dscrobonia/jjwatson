from bs4 import BeautifulSoup
import requests

FD_PRICES_FILE = "fd_prices.csv"
FD_PRICES_HIST_FILE = "fd_prices_hist_wk{0}.csv"
CURRENT_WEEK_URL = 'http://rotoguru1.com/cgi-bin/fstats.cgi?pos=0&sort=4&game=f&colA=0&daypt=0&xavg=0&inact=0&maxprc=99999&outcsv=1'
HISTORICAL_WEEK_URL = 'http://rotoguru1.com/cgi-bin/fyday.pl?week={0}&game=fd&scsv=1'

getCurrentWeek = False
getHistoricalWeek = True

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
