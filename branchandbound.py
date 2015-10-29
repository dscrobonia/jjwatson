def
   










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
