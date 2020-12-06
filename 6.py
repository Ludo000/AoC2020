def part1():
   # part 1
   print("# part1:")
   f = open("input6.txt", "r")
   counts = []
   current_group = set()
   lines = f.readlines()
   f.close()

   for n_line, line in enumerate(lines):
      current_group.update(set(line.replace("\n", "")))
      if(len(line) == 1 or n_line == len(lines) - 1): 
         counts.append(len(current_group))
         current_group = set()
   
   print("total: ", sum(counts))

def part2():
   # part 2
   print("# part2:")
   f = open("input6.txt", "r")
   count_line = 0
   counts = []
   lines = f.readlines()
   current_group = ""
   f.close()

   for n_line, line in enumerate(lines):
      if(len(line) > 1):
         count_line += 1
         current_group += line.replace("\n", "")
      if(len(line) == 1 or n_line == len(lines) - 1): 
         set_char = set()
         for c in current_group:
            if(current_group.count(c) == count_line):
               set_char.update(c)
         counts.append(len(set_char))
         count_line = 0
         current_group = ""
            
   print("total: ", sum(counts))

def main():
   part1()
   part2()

if __name__ == "__main__":
    main()