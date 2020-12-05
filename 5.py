from parse import *

def main():
   # part 1
   print("# part1:")
   rows_start = 0
   rows_end = 127
   col_start = 0
   col_end = 7
   seats = []
   f = open("input5.txt", "r")
   for line in f:
      rows_start = 0
      rows_end = 127
      col_start = 0
      col_end = 7
      line.replace("\n", "")
      for k,c in enumerate(line):
         if(c == "F" or c == "B"):
            r = round((rows_end - rows_start)/2)
            if(c == "F"): 
               rows_end -= r
               if(k == 6):
                  row = min(rows_start,rows_end)
               else:
                  row = rows_end
            else: 
               rows_start += r
               if(k == 6):
                  row = max(rows_start,rows_end)
               else:
                  row = rows_start
         elif(c == "L" or c == "R"):
            r = round((col_end - col_start)/2)  
            if(c == "L"): 
               col_end -= r
               if(k == 9):
                  col = min(col_start,col_end)
               else:
                  col = col_end
            else: 
               col_start += r
               if(k == 9):
                  col = max(col_start,col_end)
               else:
                  col = col_start
      seat_ID = row * 8 + col
      seats.append(seat_ID)
   seats.sort()
   max_seat = max(seats)
   print(max_seat)

   #part2

   print("# part2:")
   all_seats = set(range(min(seats), max(seats)+1))
   missing_seats = all_seats - set(seats)
   print(missing_seats)


if __name__ == "__main__":
    main()