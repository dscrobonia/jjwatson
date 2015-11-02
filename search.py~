import sys
from Queue import PriorityQueue

class Item:
   
   def __init__(self, index, value, weight):
      self.index = index
      self.value = value
      self.weight = weight
      self.ratio = value/weight

   def __init__(self, args):
      self.index = int(args[0])
      self.value = int(args[1])
      self.weight = int(args[2])
      self.ratio = float(self.value)/float(self.weight)

   def __lt__(self, other):
      return self.ratio < other.ratio

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

class Search:
   def greedy(capacity, size, items):
      weight = 0
      value = 0
      indices = []

      items.sort(reverse=True)

      while (weight + items[0].weight < capacity):
         temp = items.pop(0)
         weight += temp.weight
         value += temp.value
         indices.append(temp.index)

      indices.sort()

      print 'greedy solution is: ' + str(value) + ' ' + str(weight)

      print ' '.join(str(indices))



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
   capacity = 0
   size = 0
   gItems = []
   items = []
   
   if len(sys.argv) < 2:
      print "not enought arguments"
      sys.exit()

   with open(sys.argv[1]) as inFile:
      size = int(inFile.next())

      for i in range(1,size+1):
         row = inFile.next()
         gItems.append(Item([word for word in row.split()]))
         items.append([word for word in row.split()])

      capacity = int(inFile.next())

      Search.greedy(capacity, size, gItems)
      #branch(capacity, size, items, gItems)
