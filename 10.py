def part1(data):
   print("# part1:")
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
   tab_arr = []
   arr = []
   arr.append(0)
   tab_arr.append(arr)
   data.append(0)
   data.sort()
   print(data)
   i_a=0
   while i_a <= len(tab_arr)-1:
      current_c = 0
      k=0
      for i_c,c in enumerate(data):
         if (int(c) >= max(tab_arr[i_a])):
            current_c = int(c)
            k = i_c
            break
      start = k
      end = k+3
      if(end > len(data)-1): end = len(data)-1

      print("current_c: ", current_c)
      sub = []
      
      for d in range(start, end+1):
         if(data[d] > current_c and data[d] <= current_c+3):
            sub.append(data[d])
      #print("sub: ",sub)
      if(len(sub)>=1):
         #print("old a: ", tab_arr[i_a])
         #print("adding: ", sub[0])
         aa = tab_arr[i_a].copy()
         aa.append(sub[0])
         #print("new a: ", aa)
      if(len(sub)>1):
         for s in range(1, len(sub)):
            b = tab_arr[i_a].copy()
            b.append(sub[s])
            #print("new array :", b)
            tab_arr.append(b)
      tab_arr[i_a] = aa

      
      if(current_c == max(data)):
         i_a += 1
   #set_arr = set(tuple(row) for row in tab_arr)
   print()
   # for a in tab_arr:
   #    print(a)
   print(len(tab_arr))
def main():
   f = open("input10.txt", "r")
   lines = f.readlines()
   f.close()
   data = []
   for line in lines:
      data.append(int(line.rstrip("\n")))
   
   #data.append(max(data) + 3)
   data.sort()
   #print(part1(data))
   part2(data)

if __name__ == "__main__":
    main()