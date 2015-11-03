import sys
from Queue import PriorityQueue

class Player:
   
   def __init__(self, name, position, value, weight):
      self.name = name
      self.position = position
      self.value = value
      self.weight = weight
      if weight != 0:
          self.ratio = value/weight
      else:
          self.ratio = 0

   def __init__(self, args):
      self.name = str(args[0])
      self.position = str(args[1])
      self.value = float(args[2])
      self.weight = int(args[3])
      if self.weight != 0:
          self.ratio = self.value/self.weight
      else:
          self.ratio = 0


   def __lt__(self, other):
      return self.ratio < other.ratio

   def __iter__(self):
      for attr, value in self.__dict__.iteritems():
         yield attr, value

class Node:
   INDEX = 0
   VALUE = 1
   WEIGHT = 2

   def __init__(self, value, weight, bound, length, bitString):
      self.value = value
      self.weight = weight
      if weight != 0:
         self.ratio = value/weight
      else:
         weight = 0
      self.bound = bound
      self.length = length
      self.bitString = bitString

   def make_left(self, items, capacity, ratios):
      ret = Node(self.value, 
                  self.weight,
                  0,
                  self.length + 1, 
                  self.bitString + '0')
      ret.find_upper_bound(ratios, capacity)

      return ret


   def make_right(self, items, capacity, ratios):
      ret = Node(self.value + int(items[self.length][Node.VALUE]),
                  self.weight + int(items[self.length][Node.WEIGHT]), 
                  0,
                  self.length + 1, 
                  self.bitString + '1')
      ret.find_upper_bound(ratios, capacity)

      return ret

   def find_upper_bound(self, items, capacity):
      tWeight = self.weight
      v = self.value

      for i in range(0,len(items)):
         item = items[i]

         if item.index > self.length:
            if tWeight + item.weight > capacity:
               self.bound = v + (capacity - tWeight) * item.ratio
               return

            v = v + item.value
            tWeight = tWeight = item.weight
       
      self.bound = v + (capacity - tWeight) * items[0].ratio

   def __lt__(self, other):
      return self.bound < other.bound

def greedy(players, structure, capacity, numberReturned):
   weight = 0
   value = 0
   optimalLineups = []
   optimalLineup = []

   players.sort(reverse=True)

   while (structure['total'] > 0):
      temp = players.pop(0)

      if weight + temp.weight < capacity:
         weight += temp.weight
         value += temp.value
         optimalLineup.append(temp)

         #decrement players at position in lineup and total players
         #and then remove if position is filled
         structure[temp.position] = structure[temp.position] - 1
         structure['total'] = structure['total'] - 1;

         if structure[temp.position] <= 0:
            #removes players from that position
            players = filter(lambda player: player.position != temp.position, players)
            #players = [player for player in players if player.position = temp.position]
            players.sort(reverse=True)

   optimalLineup.sort()
   optimalLineups.append(optimalLineup)

   #print 'greedy solution is: ' + str(value) + ' ' + str(weight)
   #for player in optimalLineup:
   #   print player.name

   return optimalLineups


def branch(capacity, size, items, ratios):
   q = PriorityQueue()
   temp = Node(0, 0, ratios[0].ratio * capacity, 0, '')
   maxV = temp

   q.put(temp)

   while(not q.empty()):
      temp = q.get()
      print maxV.value

      if (temp.bound > maxV.value and temp.length < size):
         left = temp.make_left(items, capacity, ratios)

         if (left.bound > maxV.value):
            q.put(left)

         if (temp.weight + int(items[temp.length][Node.WEIGHT]) <= capacity):
            right = temp.make_right(items, capacity, ratios)
            if (right.value > maxV.value):
               maxV = right

            if (right.bound > maxV.value):
               q.put(right)

   print 'Using Branch and Bound the best feasible solution found (that David wrote, its probably soso): '
   
   print str(maxV.value) + ' ' + str(maxV.weight)
   for i in range(maxV.bitString):
      if (maxV.bitString[i] == '1'):
         print items[i]

if __name__ == '__main__':
   steve = Player(['steve smith', 'WR', '4.5', '600'])
   print steve
   for value in steve:
      print value


#   capacity = 0
#   size = 0
#   gPlayers = []
#   players = []
   
#   if len(sys.argv) < 2:
#      print "not enought arguments"
#      sys.exit()

#   with open(sys.argv[1]) as inFile:
#      size = int(inFile.next())

#      for i in range(1,size+1):
#         row = inFile.next()
#         gPlayers.append(Player([word for word in row.split()]))
#         players.append([word for word in row.split()])

#      capacity = int(inFile.next())

#      Search.greedy(capacity, size, gPlayerss)
      #branch(capacity, size, players, gPlayers)
