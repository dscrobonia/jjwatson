/**
 * CPE 349 Final Assignment: Knapsack Comparison
 *
 * @author David Scrobonia
 */

//imports
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.lang.Math;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Iterator;

class Item implements Comparable{
   public int index;
   public int value;
   public int weight;
   public double ratio;

   public Item(int index, int value, int weight) {
      this.index = index;
      this.value = value;
      this.weight = weight;
      this.ratio = (double)value/(double)weight;
   }
 
   public int compareTo(Object item) {
      if (this.ratio < ((Item)item).ratio)
         return 1;
      else
         return -1;
   }
}

class Node implements Comparable {
   //constants
   private static final int INDEX = 0;
   private static final int VALUE = 1;
   private static final int WEIGHT = 2;

   public int value;
   public int weight;
   public double ratio;
   public double bound;
   public String bitString;
   public int length;

   public Node() {

   }

   public Node(int value, int weight, double bound, int length, String bitString) {
      this.value = value;
      this.weight = weight;
      this.ratio = (double)value/(double)weight;
      this.bound = bound;
      this.length = length;
      this.bitString = bitString;
   }

   public Node makeLeft(int [][] items, int capacity, ArrayList<Item> ratios) {
      Node ret = new Node();
      ret.value = this.value;
      ret.weight = this.weight;
      ret.length = this.length + 1;
      ret.bitString = this.bitString + '0';
      ret.findUpperbound(ratios, capacity);
      
      return ret;
   }

   public Node makeRight(int [][] items, int capacity, ArrayList<Item> ratios) {
      Node ret = new Node();
      ret.value = this.value + items[this.length][VALUE];
      ret.weight = this.weight + items[this.length][WEIGHT];
      ret.bound = 0;
      ret.length = length + 1;
      ret.bitString = this.bitString + '1';
      ret.findUpperbound(ratios, capacity);

      return ret;
   }

   // BOUND FUNCTION
   // items is sorted list of Item by value-per-weight
   public void findUpperbound(ArrayList<Item> items, int capacity) {
      double tWeight = this.weight;
      double v = this.value;
      Item item = null;

      for (int i=0; i < items.size(); i++) {
         item = items.get(i);
         if (item.index > this.length) {
            if (tWeight + item.weight > capacity) {
               this.bound = v + (capacity - tWeight) * item.ratio;
               return;
            }
            v += item.value;
            tWeight += item.weight; 
         }
      }
      this.bound = v + (capacity - tWeight) * items.get(0).ratio;
   }

   public int compareTo(Object node) {
      if (this.bound < ((Node)node).bound)
         return 1;
      else
         return -1;
   }
}

public class KnapsackComp {
   //constants
   private static final int INDEX = 0;
   private static final int VALUE = 1;
   private static final int WEIGHT = 2;

   //Driver
   public static void main(String args[]) {
      int capacity = 0;
      int size = 0;
      int [][] items = null;

      //init
      if (args.length < 1) {
         print("not enough arguments");
         return;
      }

      Scanner scanner
      try {
         scanner = new Scanner(new File(args[0]));
      } catch (Exception FileNotFoundException) {
         print(args[0] + " does not exist");
         return;
      }

      size = scanner.nextInt();
      items = new int[size][3];

      for (int i=0; i<size; i++) {
         items[i][INDEX] = scanner.nextInt();
         items[i][VALUE] = scanner.nextInt();
         items[i][WEIGHT] = scanner.nextInt();
      }
      capacity = scanner.nextInt();

      //Full Enumeration
      long start;
      if (args[0].contains("easy20.txt")) {
         start = System.nanoTime();
         brute(capacity, size, items);
         System.out.println("brute time: " + (System.nanoTime() - start));
      } 

      //Greedy
      start = System.nanoTime();
      ArrayList<Item> gItems = new ArrayList<Item>();

      for (int i=0; i<items.length; i++) {
         gItems.add(new Item(items[i][INDEX], items[i][VALUE], items[i][WEIGHT]));
      }

      greedy(capacity, size, gItems);
      System.out.println("greedy time: " + (System.nanoTime() - start));

      //Dynamic Programming
      start = System.nanoTime();
      dynamic(capacity, size, items);
      System.out.println("dyn time: " + (System.nanoTime() - start));

      //Branch and Bound
      start = System.nanoTime();
      gItems = new ArrayList<Item>();

      for (int i=0; i<items.length; i++) {
         gItems.add(new Item(items[i][INDEX], items[i][VALUE], items[i][WEIGHT]));
      }

      Collections.sort(gItems);

      branch(capacity, size, items, gItems);
      System.out.println("branch time: " + (System.nanoTime() - start));

   }

   //helper functions
   public static void print(String s) {
      System.out.println(s);
   }

   //main functions
   public static void brute(int capacity, int size, int [][] items) {
      String maxStr = "";
      int maxValue = 0;
      int maxWeight = 0;
      int numSets = (int)Math.pow(2.0, (double)size);

      for (int i=0; i<numSets; i++) {
         int weight = 0;
         int value = 0;
         String bin = Integer.toBinaryString(i);

         for (int j=0; j<bin.length(); j++) {
            if (bin.charAt(bin.length()-j-1) == '1') {
               value += items[j][VALUE];
               weight += items[j][WEIGHT];
            }
         }

         if (value > maxValue && weight <= capacity) {
            maxValue = value;
            maxWeight = weight;
            maxStr = bin;
         }
      }

      //print results
      System.out.print("Using Brute force the best feasible solution found: ");
      System.out.println("" + maxValue + " " + maxWeight);
      for (int i=0; i<maxStr.length(); i++) {
         if (maxStr.charAt(maxStr.length()-i-1) == '1') {
            System.out.print((i+1) + " ");
         }
      }
      System.out.println("\n");
   }

   public static void greedy(int capacity, int size, ArrayList<Item> items) {
      int weight = 0;
      int value = 0;
      ArrayList<Integer> indices = new ArrayList<Integer>();
      Item temp = null;

      //TODO: justification for val/weight ratio
      Collections.sort(items);

      while (weight + items.get(0).weight < capacity) {
         temp = items.remove(0);
         weight += temp.weight;
         value += temp.value;
         indices.add(temp.index);
      }

      //sort indices
      Collections.sort(indices);

      //print results
      System.out.print("Greedy solution (not necessarily optimal): ");
      System.out.println(value + " " + weight);
      for (int index : indices) {
         System.out.print(index + " ");
      }
      System.out.println("\n");
   }

   //source: http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/
   public static void dynamic(int capacity, int size, int [][] items) {
      int [][] table = new int[size+1][capacity+1];

      //build table
      for (int i=0; i<=size; i++) {
         for (int j=0; j<=capacity; j++) {
            if (i==0 || j==0) {
               table[i][j] = 0;
            }
            else if (items[i-1][WEIGHT] <= j) {
               table[i][j] = Math.max(items[i-1][VALUE] + table[i-1][j-items[i-1][WEIGHT]], table[i-1][j]);
            }
            else {
               table[i][j] = table[i-1][j];
            }
         }
      }

      ArrayList<Integer> indices = new ArrayList<Integer>();
      int i = size;
      int j = capacity;
      int weight = 0;

      while (table[i][j] != 0) {
         if (items[i-1][WEIGHT] <= j) {
            if (items[i-1][VALUE] + table[i-1][j-items[i-1][WEIGHT]] > table[i-1][j]) {
               j -= items[i-1][WEIGHT];
               weight += items[i-1][WEIGHT];
               if (i > 0)
                  indices.add(i);
            }
         }
            i -= 1;
      }

      //order indices
      Collections.sort(indices);

      //print results
      System.out.print("Dynamic Programming solution: ");
      System.out.println(table[size][capacity] + " " + weight);
      for (int index : indices) {
         System.out.print(index + " ");
      }
      System.out.println("\n");
   }

   public static void branch(int capacity, int size, int [][] items, ArrayList<Item> ratios) {
      PriorityQueue<Node> q = new PriorityQueue<Node>();
      Node temp = new Node(0, 0, ratios.get(0).ratio*capacity, 0, "");
      Node max = temp;

      q.add(temp);

      while (!q.isEmpty()) {
         temp = q.poll();

         if (temp.bound > max.value && temp.length < size) {
            Node left = temp.makeLeft(items, capacity, ratios);

            if (left.bound > max.value) {
               q.add(left);
            }

            if (temp.weight + items[temp.length][WEIGHT] <= capacity) {
               Node right = temp.makeRight(items, capacity, ratios);
               if (right.value > max.value) {
                  max = right;
               }
               if (right.bound > max.value)
                  q.add(right);
            }
         }
      }

      System.out.println("Using Branch and Bound the best feasible solution found: ");

      print(max.value + " " + max.weight);
      for (int i=0; i<max.bitString.length(); i++) {
         if (max.bitString.charAt(i) == '1')
            System.out.print((i+1) + " ");
      }
      System.out.println("\n");
   }
}
