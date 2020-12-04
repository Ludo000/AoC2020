import re

#part 1
def part1():
   print("# part 1:")
   count = 0

   fields = {
      'byr': False,
      'iyr': False,
      'eyr': False,
      'hgt': False,
      'hcl': False,
      'ecl': False,
      'pid': False
   }
   f = open("input4.txt", "r")
   lines = f.readlines()
   f.close()
   print("len(lines)", len(lines))
   for n_line, line in enumerate(lines):
      for k in fields:
         if k in line: fields[k] = True
      if((len(line) == 1) or (n_line == len(lines) - 1)): 
         all_true = True
         for k in fields:
            if(fields[k] == False): all_true = False
            fields[k] = False
         if(all_true): count +=1
      print("n_line :", n_line)
      print(line)
      print(fields)
      print("count: ", count)
      print("_")
   print("PART1 TOTAL: ", count)

#PART 2
def sep_unit(s=""):
   for i,c in enumerate(s):
    if not c.isdigit():
        break
   return int(s[:i]), s[i:]

def print_validating(val_name, test, s):
   print(val_name)
   print("validating: ", s)
   if(test):
      print("result: OK")
   else:
      print("result: KO")

class Limit:
   n_min=0
   n_max=0

   def __init__(self, n_min, n_max):
      self.n_min = n_min
      self.n_max = n_max


class DateValidator:
   n_min = 0
   n_max = 0

   def __init__(self, n_min, n_max):
      self.n_min = n_min
      self.n_max = n_max

   def validate(self, s=""):
      r = int(s)>= self.n_min and int(s)<= self.n_max and re.match("^\d{4}$", s)
      print_validating(self.__class__, r, s)
      return r
   
class HeightValidator:
   limit = {
   "cm" : Limit(150, 193),
   "in" : Limit(59, 76)
   }

   def validate(self, s=""):
      number, unit = sep_unit(s)
      r = unit in ["cm", "in"] and number >= self.limit[unit].n_min and number <= self.limit[unit].n_max
      print_validating(self.__class__, r, s)
      return r

class ColorHexValidator:
   def validate(self, s=""):
      r = re.match("^#([a-f0-9]{6})$",s)
      print_validating(self.__class__, r, s)
      return r

class EyeColorValidator:
   def validate(self, s=""):
      r = re.match("^amb|blu|brn|gry|grn|hzl|oth$", s)
      print_validating(self.__class__, r, s)
      return r

class PassIDValidator:
   def validate(self, s=""):
      r = re.match("^\d{9}$", s)
      print_validating(self.__class__, r, s)
      return r

def part2():
   print("# part 2:")
   count = 0

   fields = {
      'byr': { 'isPresent': False, 'validator': DateValidator(1920, 2002)},
      'iyr': { 'isPresent': False, 'validator': DateValidator(2010, 2020)},
      'eyr': { 'isPresent': False, 'validator': DateValidator(2020, 2030)},
      'hgt': { 'isPresent': False, 'validator': HeightValidator()},
      'hcl': { 'isPresent': False, 'validator': ColorHexValidator()},
      'ecl': { 'isPresent': False, 'validator': EyeColorValidator()},
      'pid': { 'isPresent': False, 'validator': PassIDValidator()},
   }
   f = open("input4.txt", "r")
   lines = f.readlines()
   f.close()
   for n_line, line in enumerate(lines):
      if (len(line) > 1):
         split = line.split(" ")
         for s in split:
               ss = s.split(":")
               for k in fields:
                  if ss[0] == k and fields[k]["validator"].validate(ss[1].replace("\n", "")): fields[k]["isPresent"] = True
      if((len(line) == 1) or (n_line == len(lines)-1)): 
            all_true = True
            for k in fields:
               if(fields[k]["isPresent"] == False): all_true = False
               fields[k]["isPresent"] = False
            if(all_true): count +=1
      print("n_line :", n_line)
      print(line)
      print(fields)
      print("count ", count)
      print("_______________")
   print("PART2 TOTAL: ", count)


def main():
   part1()
   part2() 
   
if __name__ == "__main__":
    main()