import csv 
import Search

def search(players, structure, numLineups):
   optimalLineups = Search.greedy(players, structure, numLineups)

   return optimalLineups

def read_players():
   players = []

   with open('players.csv', 'rb') as playersFile:
      csvReader = csv.reader(playersFile)
      for row in csvReader:
         players.append([player for player in row])

   return players


if __name__ == '__main__':
   #list of players (player, position, price, points)
   lineupStructure = {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'K': 1, 'DEF': 1}
   players = read_players()
   numLineups = 10

   optimalLineups = search(lineupStructure, players, numLineups)

   print optimalLineups

