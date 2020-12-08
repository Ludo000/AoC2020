def run(skip_it):
   f = open("input8.txt", "r")
   lines = f.readlines()
   f.close()
   operations = []
   values = []
   pristines = []
   accumulator = 0
   skip_cont = 1
   i = 0
   j = 0

   for line in lines:
      splited = line.rstrip("\n").split(" ")
      operations.append(splited[0].strip())
      values.append(splited[1].strip())
      pristines.append(True)


   while i < len(operations) and j < len(operations):
      j += 1
      if(pristines[i]):
         pristines[i] = False
         if(operations[i] == "acc"):
            accumulator += get_op_val(values, i)
            i += 1
         elif(operations[i] == "jmp"):
            jmp_val = get_op_val(values, i)
            if(skip_it > 0 and skip_cont == skip_it):
               i += 1
            else:
               i += jmp_val
            skip_cont += 1
         else:
            i += 1
   return i == len(operations), accumulator
      
def get_op_val(values, i):
   return get_n(values, i)*int(values[i][1:len(values[i])])

def get_n(values, i):
   n = 1
   operator = values[i][0]
   if(operator == "-"):
      n = -1
   return n

def main():
   ok = False
   print("# part1:")
   ok, accumulator = run(0)
   print("accumulator: ", accumulator)

   print("# part2:")
   ok = False
   i = 1
   while not ok:
      ok, accumulator = run(i)
      i += 1
   print("accumulator: ", accumulator)

if __name__ == "__main__":
    main()