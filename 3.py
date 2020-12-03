from parse import *

def main():
   # part 1
   print("# part1:")
   i = 0
   tree_count = 0
   f = open("input3.txt", "r")
   for line in f:
      m = i % (len(line) - 1)
      if(line[m] == '#'): tree_count += 1
      i += 3
   print("total : ", tree_count)


   # part 2
   print("\n# part2:")
   total = 1
   right = [1,3,5,7,1]
   down = [1,1,1,1,2]
   for k,r in enumerate(right):
      f = open("input3.txt", "r")
      i = 0
      l = 0
      tree_count = 0
      lines = f.readlines()
      while l < len(lines):
         line = lines[l]
         m = i % (len(line) - 1)
         if(line[m] == '#'): tree_count += 1
         i += r
         l += down[k]
      print("tree count: ", tree_count)
      total *= tree_count
      f.close()
   print("total: ", total)


if __name__ == "__main__":
    main()