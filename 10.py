def part1(data):
   print("# part1:")
   data.sort()
   data.append(max(data) + 3)
   i=0
   distri = []
   for c in data:
      if(int(c) > i and int(c) <= i+3):
         distri.append(int(c) - i)
         i = int(c)
      else:
         break
   n_1 = 0
   n_3 = 0
   for n in distri:
      if(n == 1): n_1 += 1
      elif(n == 3): n_3 += 1
   return n_1 * n_3



def part2(data):
   print("# part2:")
   data.append(0)
   data.sort()
   data.reverse()
   combis = {}
   for i, d in enumerate(data) :
      ok = []
      for j in range(1,4):
         k = i+j
         if(k > len(data)-1): k = len(data)-1
         if(data[k]<data[i] and data[k]>=data[i]-3):
            ok.append(data[k])
      combis[int(d)] = list(set(ok))

   soluce = {}
   for k in combis.keys():
       soluce[k] = 0

   for k in list(set(combis.keys())):
      for n in combis[k]:
         s = soluce[n]
         if(s == 0): s=1
         soluce[k] += s

   print(soluce[max(data)])
      

def main():
   f = open("input10.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(int(line.rstrip("\n")))
   
   print(part1(data))
   part2(data)

if __name__ == "__main__":
    main()