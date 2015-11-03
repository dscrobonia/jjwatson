import csv 
import search
from search import Player

def optimize(players, structure, salaryCap, numLineups):
   #optimalLineups = search.greedy(players, structure, salaryCap, numLineups)
   optimalLineups = search.branch(players, structure, salaryCap, numLineups)

   return optimalLineups

def read_players():
   players = []

   with open('players.csv', 'rb') as playersFile:
      csvReader = csv.reader(playersFile)
      for row in csvReader:
         players.append(Player([info for info in row]))

   return players

def get_lineups():
   #list of players (player, position, price, points)
   lineupStructure = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'D': 1}
   players = read_players()
   numLineups = 10

   optimalLineups = optimize(players, lineupStructure, 60000, numLineups)

   with open('optimal.csv', 'wb') as outFile:
      csvWriter = csv.writer(outFile)
      for lineup in optimalLineups:
         csvWriter.writerow(['new lineup'])
         for player in lineup:
            csvWriter.writerow([value[1] for value in player])

   return optimalLineups

if __name__ == '__main__':
   lineups = get_lineups()

   for lineup in lineups:
      total = 0
      cost = 0
      for player in lineup:
         total = total + player.value
         cost = cost + player.weight
         print player.name, player.value

      print 'total:', total, 'cost:', cost
