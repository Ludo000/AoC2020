def part1(data, preamble):
   print("# part1:")
   for i in range(0, len(data)):
      if(i > preamble-1):
         ok = False
         for j in range (i-preamble, i):
            for k in range (j, i):
               if(data[j] != data[k] and data[j]+data[k] == data[i]):
                  ok = True
                  break
            if(ok): break
         if(not ok):
            return data[i]

def part2(data, invalid_number):
   print("# part2:")
   for i in range(0, len(data)):
      count = 0
      res = []
      for j in range(i, len(data)):
         count += data[j]
         res.append(data[j])
         if(data[i] != invalid_number and count == invalid_number):
            return min(res) + max(res)

def main():
   f = open("input9.txt", "r")
   lines = f.readlines()
   f.close()
   data = [
   for line in lines:
      data.append(int(line.rstrip("\n")))
   invalid_number = part1(data, 25)
   print(invalid_number)
   print(part2(data, invalid_number))

if __name__ == "__main__":
    main()