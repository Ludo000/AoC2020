def part1(data):
   print("# part1:")
   data.sort()
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
   data.append(max(data)+3)
   data.append(0)
   data.sort()
   data.reverse()
   combi = {}
   for i, d in enumerate(data) :
      ok = []
      for j in range(1,4):
         k = i+j
         if(k > len(data)-1): k = len(data)-1
         if(data[k]<data[i] and data[k]>=data[i]-3):
            ok.append(data[k])
      combi[int(d)] = list(set(ok))
   print("data ok")
   print(data)
   print(combi)
   print(cal(max(data), combi, 0))


def cal(d, combi, i):
   # pre = ''
   # for j in range(0,i): 
   #    pre += '_ '
   # print(f'{pre}{d}')
   # print()
   sum_c = 0
   for c in combi[d]:
      sum_c += cal(c, combi, i+1) or 1
   return sum_c
      

def main():
   f = open("input10.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(int(line.rstrip("\n")))
   
   #data.append(max(data) + 3)
   #print(part1(data))
   part2(data)

if __name__ == "__main__":
    main()