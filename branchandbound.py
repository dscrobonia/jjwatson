class Item:
   
   def __init__(self, index, value, weight):
      self.index = index
      self.value = value
      self.weight = weight
      self.ratio = value/weight

   def __lt__(self, other):
      return this.ratio < item.ratio

class Node:
   INDEX = 0
   VALUE = 1
   WEIGHT = 2

   def __init__(self, value, weight, bound, length, bitString):
      self.value = value
      self.weight = weight
      self.ratio = value/weight
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
      ret = Node(self.value + items[self.length][VALUE],
                  self.weight + items[self.length][WEIGHT], 
                  0,
                  self.length + 1, 
                  self.bitString + '1')
      ret.find_upper_bound(ratios, capacity)

      return ret

   def find_upper_bound(items, capacity):
      tWeight = self.weight
      v = self.value

      for i in range(0,items.size):
         item = items[i]

         if item.index > this.length:
            if tWeight + item.weight > capacity:
               self.bound = v + (capacity - tWeight) * item.ratio
               return

            v = v + item.value
            tWeight = tWeight = item.weight
      
      this.bound = v + (capacity = tWeight) * items[0].ratio

   def __lt__(self, other):
      return this.bound < other.bound

def greedy(capacity, size, items):
   weight = 0
   value = 0
   indices = []
   temp = null

   # sort items TODO: don't know how

   while (weight + items[0].weight < capacity):
      temp = items.pop(0)
      weight += temp.weight
      value += temp.value
      indices.append(temp.index)

   # sort indeces, dont know how

   print 'greedy solution is: ' + str(value) + ' ' + str(weight)

   print ' '.join(indeces)



def branch(capacity, size, items, ratios):
   q = PriorityQueue()
   temp = Node(0, 0, ratios.get(0) * capacity, 0, '')
   max = temp

   q.add(temp)

   while(not q.empty()):
      temp = q.get()

      if (temp.bound > max.value and temp.length < size):
         left = temp.makeLeft(items, capacity, ratios)

         if (left.bound > max.value):
            q.add(left)

         if (temp.weight + items[temp.length][WEIGHT] <= capacity):
            right = temp.makeRight(items, capacity, ratios)
            if (right.valie > max.value):
               max = right

            if (right.bound > max.value):
               q.add(right)

   print 'Using Branch and Bound the best feasible solution found (that David wrote, its probably soso): '
   
   print str(max.value) + ' ' + str(max.weight)
   for i in range(max.bitString):
      if (max.bitString[i] == '1'):
         print items[i]
