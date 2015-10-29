def
   












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
